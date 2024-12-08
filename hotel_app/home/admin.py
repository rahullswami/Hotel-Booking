from django.contrib import admin
from .models import Hotel, HotelBooking, Contact, Hotel_Image

admin.site.register(HotelBooking)
admin.site.register(Contact)

class HotelImageAdmin(admin.StackedInline):
    model = Hotel_Image

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageAdmin]

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Hotel_Image)