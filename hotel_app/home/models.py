from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    hname = models.CharField(max_length=100)
    hdesc = models.TextField()

    def __str__(self):
        return self.hname


class Hotel_Image(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='paper_images')
    image = models.ImageField(upload_to='paper')
    

class HotelBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    datetime = models.DateTimeField(auto_now_add=True)
    destination = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.fullname +'--'+ self.email
    

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.fullname +'--'+ self.email
    