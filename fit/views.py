from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Disease, Doctors, Patient, Pharmacy, Appointment
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'fit/index.html')


def viewdoctors(request):
    username = request.user.username
    patloc = Patient.objects.get(pat_username=username)
    loc = patloc.pat_loc
    doctorsList = Doctors.objects.filter(doc_location=loc)
    appoitments = Appointment.objects.filter(patient__pat_username=username)
    params = {
        "doctorsList": doctorsList,
        "appoints": appoitments
    }
    return render(request, 'fit/viewdoctors.html', params)


def bookappointment(request):
    if request.method == "POST":
        pat = request.POST['patient']
        dc = request.POST['appointed']
        date = request.POST['date']
        app = Appointment(patient=Patient.objects.get(
            pat_username=pat), doctor=Doctors.objects.get(doc_username=dc), appointment_date=date)
        app.save()
        messages.success(request, "Appoitment Successfull")
        return redirect('/viewdoctors')


def viewpharmacy(request):
    username = request.user.username
    patient = Patient.objects.get(pat_username=username)
    loc = patient.pat_loc
    pharmacyList = Pharmacy.objects.filter(pharmay_location=loc)
    params = {
        "pharmacyList": pharmacyList
    }
    return render(request, 'fit/viewpharmacies.html', params)


def patientprofile(request):
    username = request.user.username
    profile = Patient.objects.filter(pat_username=username)
    params = {
        "profile": profile
    }
    return render(request, 'fit/patientprofile.html', params)


def pharmacyprofile(request):
    username = request.user.username
    pharm = Pharmacy.objects.filter(phar_username=username)
    params = {
        "pharm": pharm
    }
    return render(request, 'fit/pharmacyprofile.html', params)\



def doctorprofile(request):
    name = request.user.username
    profile = Doctors.objects.filter(doc_username=name)
    params = {
        "profile": profile
    }
    return render(request, 'fit/doctorprofiledashboard.html', params)


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
                messages.success(
                    request, "You are signed up kindly login with your username and password now !")
                return redirect('/')
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
                messages.success(
                    request, "You are signed up kindly login with your username and password now !")
                return redirect('/')
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
                messages.success(
                    request, "You are signed up kindly login with your username and password now !")
                return redirect('/')
            else:
                messages.warning(request, "Passwords did not match !")
                return redirect('/')

    else:
        return HttpResponse('404-Not Found')


def patientpage(request):
    username = request.user.username
    profile = Disease.objects.filter(pat__pat_username=username)
    params = {
        "profile": profile
    }
    return render(request, 'fit/patientDashboard.html', params)


def about(request):
    return render(request, 'fit/aboutus.html')


def updatepatientprofile(request):
    if request.method == "POST":
        patid = request.POST['patid']
        phone = request.POST['phone']
        add = request.POST['address']
        idproof = request.FILES['patientidProof']
        profile = Patient.objects.get(pat_id=patid)
        profile.pat_phone = phone
        profile.pat_address = add
        profile.pat_idProof = idproof
        profile.save()
        logout(request)
        messages.success(
            request, "Profile updated. You are requested to login again!")
        return redirect('/')


def updatepharmacyprofile(request):
    if request.method == "POST":
        pharid = request.POST['pharid']
        phone = request.POST['phone']
        add = request.POST['address']
        ownername = request.POST['ownername']
        idproof = request.FILES['pharmacyidProof']
        profile = Pharmacy.objects.get(phar_id=pharid)
        profile.phar_phone = phone
        profile.phar_address = add
        profile.phar_idProof = idproof
        profile.phar_ownerName = ownername
        profile.save()
        logout(request)
        messages.success(
            request, "Profile updated. You are requested to login again!")
        return redirect('/')


def updatedoctorprofile(request):
    if request.method == "POST":
        docid = request.POST['Docid']
        phone = request.POST['phone']
        add = request.POST['address']
        spl = request.POST['cat']
        idproof = request.FILES['doctoridProof']
        profile = Doctors.objects.get(doc_id=docid)
        profile.doc_phone = phone
        profile.doc_address = add
        profile.doc_idProof = idproof
        profile.doc_category = spl
        profile.save()
        logout(request)
        messages.success(
            request, "Profile updated. You are requested to login again!")
        return redirect('/')


def contactus(request):
    return render(request, 'fit/contactus.html')


def docpage(request):
    docusername = request.user.username
    doctor_patientList = Disease.objects.filter(doc__doc_username=docusername)
    appointments = Appointment.objects.filter(doctor__doc_username=docusername)

    params = {
        "patientList": doctor_patientList,
        "appointments": appointments
    }
    return render(request, 'fit/doctorDashboard.html', params)


def pharpage(request):
    patients = Disease.objects.all()
    params = {
        "allpatients": patients
    }
    return render(request, 'fit/pharmacyDashboard.html', params)


def handleLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if Patient.objects.filter(pat_username=username).count() != 0:
            login(request, user)
            return redirect('/patientprofile/')
        if Doctors.objects.filter(doc_username=username).count() != 0:
            login(request, user)
            return redirect('/doctorprofile/')
        if Pharmacy.objects.filter(phar_username=username).count() != 0:
            login(request, user)
            return redirect('/pharmacyprofile/')
    else:
        messages.error(request, "Invalid Credential")


def handleLogout(request):
    logout(request)
    messages.success(request, "You are Logged Out !")
    return redirect('/')


def addmedicine(request):
    if request.method == "POST":
        pat_name = request.POST['pat']
        disease = request.POST['dise']
        patient = Disease.objects.get(
            pat__pat_username=pat_name, disease_name=disease)
        try:
            medicine1 = request.POST['medicine1']
            patient.med1 = medicine1
            patient.save()
        except:
            print("Medicine one already there")
        try:
            medicine2 = request.POST['medicine2']
            patient.med2 = medicine2
            patient.save()
        except:
            print("Medicine two already there")
        try:
            medicine3 = request.POST['medicine3']
            patient.med3 = medicine3
            patient.save()
        except:
            print("Medicine three already there")
        try:
            medicine4 = request.POST['medicine4']
            patient.med4 = medicine4
            patient.save()
        except:
            print("Medicine four already there")
        try:
            medicine5 = request.POST['medicine5']
            patient.med5 = medicine5
            patient.save()
        except:
            print("Medicine five already there")
        try:
            medicine6 = request.POST['medicine6']
            patient.med6 = medicine6
            patient.save()
        except:
            print("required medicine added")
        messages.success(request, "Medicines added")
        return redirect('/doc')


def addpatient(request):
    if request.method == "POST":
        docuser = request.user.username
        patient = request.POST['patientusername']
        disease = request.POST['disease']
        desc = request.POST['desc']
        if Patient.objects.filter(pat_username=patient).count() != 0:
            d = Disease(pat=Patient.objects.get(pat_username=patient), doc=Doctors.objects.get(
                doc_username=docuser), disease_name=disease, disease_description=desc)
            d.save()
            return redirect('/doc')
        else:
            messages.warning("patient with this username does not exist")
            return redirect('/doc')

def blog(request):
    return render(request, 'fit/blog.html')