from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handleLogin, name="handleLogIn"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('pat/', views.patientpage, name="patientpage"),
    path('doc/', views.docpage, name="docpage"),
    path('phar/', views.pharpage, name="pharpage"),
]
