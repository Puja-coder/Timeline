from django.shortcuts import render
from django.http import HttpResponse
from .models import TimeClock
from tabulate import tabulate
import datetime


# Create your views here.

def Timeclockfn(request):
    res = list(TimeClock.objects.values('user', 'clock_in', 'clock_out'))
    list1 = []
    for i in res:
        list1.append({"userid ": i['user'], "clock in ": i['clock_in'], "clock out ": i['clock_out'], "Total hour worked ": (i['clock_out']-i['clock_in'])})
    return HttpResponse(list1)

