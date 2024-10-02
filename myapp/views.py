
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Import the User model to create new users
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages  # Import Django's messaging framework to display messages
from .models import Feature

def index(request):
    features = Feature.objects.all()
    # Pass the list to the template using the key 'features'
    return render(request, 'index.html', {'features': features})


# Function to handle user registration
def register(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Get the form data from the POST request
        username = request.POST['username']  # Retrieve the 'username' input value
        email = request.POST['email']        # Retrieve the 'email' input value
        password = request.POST['password']  # Retrieve the 'password' input value
        confirm_password = request.POST['confirm_password']  # Retrieve the 'confirm_password' input value


        # Check if the entered passwords match
        if password == confirm_password:
            # Check if the username is not already taken
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('register')
                # Check if the email is not already registered
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            else:
                # Create a new user if all conditions are satisfied
                user =  User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful! You can now log in.')

                return redirect('login')  # Redirect the user to the login page
            
        else:
            # Display an error if the passwords do not match
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    

    return render(request, 'register.html')

def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')

    return render (request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})









