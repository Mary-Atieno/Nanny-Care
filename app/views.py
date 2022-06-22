from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import User

# Create your views here.
def Index(request):


    return render(request, 'index.html')

def booking(request):
    return render(request, 'book/booking.html')


@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    context = {
        'user': user
    }
    return render(request, 'profile/profile.html', context)
