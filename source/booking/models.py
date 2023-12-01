from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=200)
    ic = models.CharField(max_length=100)
    disease = models.CharField(max_length=200, default='')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookingdetails'


class BookingChecker(models.Model):
    date = models.DateField(primary_key=True)  # Use 'date' as the primary key
    slot_9am = models.BooleanField(default=True)
    slot_11am = models.BooleanField(default=False)
    slot_1pm = models.BooleanField(default=False)
    slot_3pm = models.BooleanField(default=False)
    slot_5pm = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookingchecker'
