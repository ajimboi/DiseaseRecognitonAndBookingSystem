from django.contrib import admin
from .models import Booking
class BookingInLine(admin.ModelAdmin):
    model = Booking

admin.site.register(Booking, BookingInLine)
# Register your models here.
