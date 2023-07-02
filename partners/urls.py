from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('',PartnerLanding,name='landing'),
    path('dashboard/',DashBoard,name='dashboard'),
    path('profile/',ProfilePage,name='profile'),
    path('register/<acc>/',RegisterPartner,name='register'),
    path('sign-in',Login,name='login'),
    path('invoice',GenerateInvoice,name='create-invoice'),
    path('forgot-password/',TemplateView.as_view(template_name='forgot-password.html'),name='forgot-password'),
    path('logout/',Logout,name='logout')
]

