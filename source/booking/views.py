from django.shortcuts import render, redirect
from .models import Booking, BookingChecker
from django.db import connection

def booking(request):
    if request.method == 'POST':
        form_data = request.POST
        name = form_data['name']
        ic = form_data['ic_number']
        disease = form_data['disease_you_have']
        description = form_data['description']
        booking_date = form_data['booking_date']  # Make sure this field is included in the template
        location = form_data['clinic_or_hospital']
        time_slot = form_data['time_slot']

        # Update the bookingchecker table based on the selected time_slot
        with connection.cursor() as cursor:
            if time_slot == '9am':
                cursor.execute("""
                    UPDATE bookingchecker SET slot_9am = 0 WHERE date = %s
                """, [booking_date])
            elif time_slot == '11am':
                cursor.execute("""
                    UPDATE bookingchecker SET slot_11am = 0 WHERE date = %s
                """, [booking_date])
            elif time_slot == '1pm':
                cursor.execute("""
                    UPDATE bookingchecker SET slot_1pm = 0 WHERE date = %s
                """, [booking_date])
            elif time_slot == '3pm':
                cursor.execute("""
                    UPDATE bookingchecker SET slot_3pm = 0 WHERE date = %s
                """, [booking_date])
            elif time_slot == '5pm':
                cursor.execute("""
                    UPDATE bookingchecker SET slot_5pm = 0 WHERE date = %s
                """, [booking_date])

        # Insert data into bookingdetails table
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO bookingdetails (name, ic, disease, description, date, time_slot, location)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, [name, ic, disease, description, booking_date, time_slot, location])

        return render(request, 'success.html', {'booking': form_data})

    return render(request, 'booking.html')

def bookingChecker(request):
    if request.method == 'POST':
        booking_date = request.POST.get('date')

        # Redirect back to the booking page if the booking_date is not provided
        if not booking_date:
            return redirect('Booking')

        # Retrieve the BookingChecker object for the selected date
        try:
            checker = BookingChecker.objects.filter(date=booking_date).first()
        except BookingChecker.DoesNotExist:
            checker = None

        # Call the function to get bookingchecker data
        bookingchecker_data = get_bookingchecker_data(booking_date)

        # Pass the availability information to the template
        context = {
            'booking_date': booking_date,
            'checker': checker,
            'bookingchecker_data': bookingchecker_data,
        }

        return render(request, 'booking.html', context)

    # Redirect to the booking page if accessed directly without POST
    return redirect('Booking')

    # Redirect to the booking page if accessed directly without POST
    return redirect('Booking')

def get_bookingchecker_data(booking_date):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT slot_9am, slot_11am, slot_1pm, slot_3pm, slot_5pm, date
            FROM bookingchecker WHERE date = %s
        """, [booking_date])
        rows = cursor.fetchall()

        # Process the data and return a list of dictionaries
        bookingchecker_data = []
        for row in rows:
            slot_9am, slot_11am, slot_1pm, slot_3pm, slot_5pm, date = row
            bookingchecker_data.append({
                'date': date,
                'slot_9am': slot_9am,
                'slot_11am': slot_11am,
                'slot_1pm': slot_1pm,
                'slot_3pm': slot_3pm,
                'slot_5pm': slot_5pm,
            })

        return bookingchecker_data