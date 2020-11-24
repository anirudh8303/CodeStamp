from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Disease, Doctors, Patient, Pharmacy
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'fit/index.html')


def patientpage(request):
    return render(request, 'fit/patientDashboard.html')


def docpage(request):
    return render(request, 'fit/doctorDashboard.html')


def pharpage(request):
    return render(request, 'fit/pharmacyDashboard.html')


def handleSignUp(request):
    if request.method == "POST":
        email1 = request.POST['email1']
        fname = request.POST['fname']
        username = request.POST['username1']
        loc = request.POST['loc']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        chck = request.POST['chklgin']
        if chck == "Patient":
            if pass1 == pass2:
                myuser = User.objects.create_user(username, email1, pass1)
                myuser.save()
                pat = Patient(pat_username=username, pat_loc=loc,
                              pat_name=fname, pat_email=email1)
                pat.save()
                return redirect('/pat')
            else:
                messages.warning(request, "Passwords did not match !")
                return redirect('/')
        if chck == "Doctor":
            if pass1 == pass2:
                myuser = User.objects.create_user(username, email1, pass1)
                myuser.save()
                doc = Doctors(doc_username=username, doc_location=loc,
                              doc_name=fname, doc_email=email1)
                doc.save()
                return redirect('/doc')
            else:
                messages.warning(request, "Passwords did not match !")
                return redirect('/')
        if chck == "Pharmacist":
            if pass1 == pass2:
                myuser = User.objects.create_user(username, email1, pass1)
                myuser.save()
                ph = Pharmacy(phar_username=username, pharmay_location=loc,
                              phar_name=fname, phar_email=email1)
                ph.save()
                return redirect('/phar')
            else:
                messages.warning(request, "Passwords did not match !")
                return redirect('/')

    else:
        return HttpResponse('404-Not Found')


def handleLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if Patient.objects.filter(pat_username=username).count() != 0:
            login(request, user)
            return redirect('/pat')
        if Doctors.objects.filter(doc_username=username).count() != 0:
            login(request, user)
            return redirect('/doc')
        if Pharmacy.objects.filter(phar_username=username).count() != 0:
            login(request, user)
            return redirect('/phar')
    else:
        messages.error(request, "Invalid Credential")


def handleLogout(request):
    logout(request)
    messages.success(request, "You are Logged Out !")
    return redirect('/')
