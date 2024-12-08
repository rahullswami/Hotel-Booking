from django.shortcuts import render, redirect, get_object_or_404
from .models import Hotel, HotelBooking, Contact,Hotel_Image
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    hotels = Hotel.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        hotels = Hotel.objects.filter(
        Q(hname__icontains = search)|
        Q(hdesc__icontains = search)
        )
        
    return render(request, 'index.html',{'hotels':hotels})

@login_required(login_url='login')
def hotel_details(request, id):
    hotel = get_object_or_404(Hotel, id=id)
    return render(request, 'hotels_details.html', {'hotel':hotel})


@login_required(login_url='login')
def booking(request):
    hotels = Hotel.objects.all()
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        datetime = request.POST.get('datetime')
        destination = request.POST.get('destination')
        message = request.POST.get('message')

        user = HotelBooking.objects.filter(email=email, user=request.user)
        if user.exists():
            messages.info(request, 'Email is already use')
            return redirect('booking')

        user = HotelBooking.objects.create(
            user=request.user,
            fullname=fullname,
            email=email,
            datetime=datetime,
            destination=destination,
            message=message,
        )
        
        user.save()
        messages.success(request, 'Your Hotel is Book successfullly')
        return redirect('yourhotel')

    return render(request, 'booking.html', {'hotels':hotels})


@login_required(login_url='login')
def update_booking(request, id):
    hotels = Hotel.objects.all()
    booking = get_object_or_404(HotelBooking, id=id)

    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        destination = request.POST.get('destination')
        message = request.POST.get('message')

        booking.fullname = fullname
        booking.email = email
        booking.destination = destination
        booking.message = message

        booking.save()

        messages.success(request, 'Booking Updated Successfully.')
        return redirect('yourhotel')

    return render(request, 'update_booking.html', {'booking':booking, 'hotels':hotels})


@login_required(login_url='login')
def delete_booking(request, id):
    booking = get_object_or_404(HotelBooking, id=id)
    
    if request.method == "POST":
        booking.delete()
        messages.success(request, 'Your booking has been deleted successfully')
        return redirect('yourhotel')

    return render(request, 'delete_booking.html', {'booking':booking})



@login_required(login_url='login')
def yourhotel(request):
    hotelbook = HotelBooking.objects.filter(user=request.user)
    return render(request, 'yourhotel.html',{'hotelbook':hotelbook})


@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        user = Contact.objects.create(
            fullname=fullname,
            email=email,
            subject=subject,
            message=message
        )

        user.save()
        messages.success(request, 'Your message successfullly send')
        return redirect('contact')

    return render(request, 'contact.html')