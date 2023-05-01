from django.urls import path
from .views import *
urlpatterns = [
    path('/books/',Shop_Books,name='book-shop'),
    path('/merchs/',Shop_Merchs,name='merch-shop')
]

