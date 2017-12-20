
import datetime
from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    '''
    Render the main page
    '''
    now = datetime.datetime.now()
    context = {'like':'Django 很棒', 'now':now}
    return render(request, 'main/main.html', context)



def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')

