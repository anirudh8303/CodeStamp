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
    path('updatedoctorprofile/', views.updatedoctorprofile,
         name="updatedoctorprofile")
]
