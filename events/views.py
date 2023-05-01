from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from datetime import date,datetime
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.





def sort_data_month(qs):
    date_objects={
        'January':[[],1],
        'February':[[],2],
        'March':[[],3],
        'April':[[],4],
        'May':[[],5],
        'June':[[],6],
        'July':[[],7],
        'August':[[],7],
        'September':[[],8],
        'October':[[],10],
        'November':[[],11],
        'December':[[],12],
    }
    for i in date_objects:
        date_objects[i][0]=[x for x in qs if x.event_start_date.strftime("%B")==i]
    return date_objects

def EventLanding(request):
    events=Event.objects.filter(completed=False).order_by('event_start_date')
    context=sort_data_month(events)
    print(sort_data_month(events))
    return render(request,'events.html',{'context':context,"month_now":datetime.now().month})

def PastEvents(request):

    past_events=Event.objects.filter(completed=True)
    context=sort_data_month(past_events)
    return render(request,'past-events.html',{'context':context})
