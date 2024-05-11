from django.shortcuts import render
from django.http import HttpResponse


def showtime(request):
    return HttpResponse('Request time is: {}'.format(request.current_time))
