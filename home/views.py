from django.shortcuts import render,redirect
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if request.user.is_anonymous:
     return redirect("/login")
    return render(request,'index.html')
def loginUser(request):
    if request.method == 'POST':
        # Assuming you have a login form with username and password fields
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect to a success page
            return redirect('/')
        else:
            # Return an invalid login message
            return render(request, 'login.html')
    else:
        # If it's not a POST request, just render the login form
        return render(request, 'login.html')
def logoutUser(request):
   logout(request)
   return redirect("/login")        