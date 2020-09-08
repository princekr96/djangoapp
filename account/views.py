from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Account

# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        gender = request.POST['gender']

        user = Account.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1, gender=gender)
        user.save()
        print('User created')

    else:
        return render(request, 'register.html')

