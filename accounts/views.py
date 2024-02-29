from django.shortcuts import render, redirect
from ClothApp.views import home_page

from accounts.models import Account
from .forms import RegistrationForm, UserLoginForm

from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout

from django.contrib.auth.decorators import login_required


# Create your views here.
 
def registration_form(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request,'register_form.html',{'form_data':form})
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():                 # checks data's basic validation
            form.save()                     # saves data in form("RegistrationForm") after Validation. 
            messages.success(request,"ACCOUNT CREATED SUCCESSFULLY...") # message to shows that action is successfully completed.
            return redirect('home')         # Sends user To Home page using url we set for homepage in urls.py[ClothStore]
        else:
            for field,errors in form.errors.items():    #builtIn feature of RegistrationForm in django
                # print('Error msg:',field,errors)  -- for understanding purpose
                for error in errors:
                    messages.error(request,f"{field.capitalize()} : {error}")   # gives error message of respective field.
            return render(request,'register_form.html',{'form_data':form}) # To load register form page if theres any issue creating account/s.    
    return render(request,'register_form.html',{'form_data':form})    


def login_form(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = Account.objects.get(email=email)
        if user.check_password(password):
            auth_login(request,user,backend='accounts.backends.MyBackEnd')
            messages.success(request,f'Welcome {email} You have logged in successfully. ')
            return redirect('home')
        else: 
            # print("Failed")
            messages.error(request,"Invalid Login Credentials")
            
    return render(request,'login.html')  
      
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request,f'You have logged out. ')

    return redirect('home')
 