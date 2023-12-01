from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='Booking'),  # The main booking page
    path('booking_checker/', views.bookingChecker, name='bookingChecker'),  # The booking checker page
]
