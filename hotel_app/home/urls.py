from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('hotel/detail/<int:id>/', hotel_details, name='hotel_details'),
    path('your/hotel/', yourhotel , name='yourhotel'),
    path('update-booking/<int:id>/', update_booking, name='update_booking'),
    path('delete-booking/<int:id>/', delete_booking, name='delete_booking')
]

# Super user
# username = root
# password = root