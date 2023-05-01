from django.urls import path
from .views import *
urlpatterns = [
    path('',EventLanding,name='events'),
    path('past-events',PastEvents,name='past-events')
]
