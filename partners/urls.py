from django.urls import path
from .views import *

urlpatterns = [
    path('',PartnerLanding,name='landing'),
    path('dashboard/',DashBoard,name='dashboard'),
    path('profile/',ProfilePage,name='profile'),
    path('register/<acc>/',RegisterPartner,name='register'),
    path('sign-in',Login,name='login'),
    path('invoice',GenerateInvoice,name='create-invoice')
]

