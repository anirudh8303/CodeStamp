from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handleLogin, name="handleLogIn"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('pat/', views.patientpage, name="patientpage"),
    path('doc/', views.docpage, name="docpage"),
    path('phar/', views.pharpage, name="pharpage"),
    path('about/', views.about, name="about"),
    path('contactus/', views.contactus, name="contactus"),
    path('doctorprofile/', views.doctorprofile, name="doctorprofile"),
    path('pharmacyprofile/', views.pharmacyprofile, name="pharmacyprofile"),
    path('patientprofile/', views.patientprofile, name="patientprofile"),
    path('updatedoctorprofile/', views.updatedoctorprofile,
         name="updatedoctorprofile"),
    path('updatepharmacyprofile/', views.updatepharmacyprofile,
         name="updatepharmayprofile"),
    path('updatepatientprofile/', views.updatepatientprofile,
         name="updatepatientprofile"),
    path('viewdoctors/', views.viewdoctors,
         name="viewdoctors"),
    path('viewpharmacy/', views.viewpharmacy,
         name="viewpharmacy"),
    path('bookappointment/', views.bookappointment,
         name="bookappointment"),
    path('addpatient/', views.addpatient, name="addpatient"),
    path('addmedicine/', views.addmedicine, name="addmedicine"),
     path('blog/', views.blog, name="blog"),
]
