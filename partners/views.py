from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login,logout,authenticate
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta,datetime
# Create your views here.

User=get_user_model()

def RegisterPartner(request,acc):
    print(acc)

    if request.method=='POST':
        if User.objects.filter(email=request.POST['email']):
            messages.error(request,'Account with email already exists')
        elif User.objects.filter(username=request.POST['username']):
            messages.error(request,'Account with username already exists')
        else:
            new_user=User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
            )
            new_user.set_password(request.POST['password'])
            new_user.save()
            if acc=="vip":
                new_partner=Partner.objects.create(
                user=new_user,
                account_type='VIP'
                )
                new_partner.save()
            elif acc=="exe":
                new_partner=Partner.objects.create(
                user=new_user,
                account_type='EXECUTIVE'
                )
                new_partner.save()
            elif acc=="amb":
                new_partner=Partner.objects.create(
                user=new_user,
                account_type='AMBASSADOR'
                )
                new_partner.save()
        messages.success(request,"Account creation successful")
        return redirect('login')
    return render(request,'register.html',{"type":acc})

def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.get(email=email)
        if user:
            print(user.username)
            auth_user=authenticate(username=user.username,password=password)
            if auth_user == None:
                print("invalid credentials")
                messages.error(request,'Invalid Credentials')
            else:
                print('authenticated')
                login(request, auth_user)
                return redirect('dashboard')
        else:
            messages.error(request,"Account with email doesn't exist")
        return redirect('dashboard')
    return render(request,'sign-in.html')
def PartnerLanding(request):
    return render(request,'partners.html')

@login_required(login_url='login')
def DashBoard (request):
    donations=Donation.objects.filter(partner=request.user).order_by('-id')
    return render(request,'dashboard.html',{"donations":donations})
@login_required(login_url='login')
def ProfilePage(request):
    if request.method=='POST':
        uname=request.user.username
        auth_user=authenticate(username=uname,password=request.POST['oldpw'])
        if auth_user is not None and request.POST['newpw']:
            auth_user.password=request.POST['newpw']
            auth_user.set_password(request.POST['newpw'])

            if request.FILES['profile-image']:
                auth_user.user_ref.profile_image=request.FILES['profile-image']
                auth_user.user_ref.save()
            auth_user.save()
            login(request, auth_user)
            print('Profile Updated')
        elif auth_user is not None:
            if request.FILES['profile-image']:
                auth_user.user_ref.profile_image=request.FILES['profile-image']
                auth_user.user_ref.save()
            print("No New Passowrd Given")
        elif auth_user is None and request.POST['oldpw']:
            print("Wrong Password")
        if request.FILES['profile-image']:
            request.user.user_ref.profile_image=request.FILES['profile-image']
            request.user.user_ref.save()

    return render(request,'profile.html')

@login_required(login_url='login')
def GenerateInvoice(request):
    if request.method=='POST':
        Donation.objects.create(
            verified=False,
            partner=request.user,
            contact_email=request.POST['email']
        )

        messages.success(request, "Invoice created successfully")
        return redirect('dashboard')
    return render(request,'generate-payment.html')
