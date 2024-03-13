from django.shortcuts import render
from datetime import datetime


def itenerary(request):
    return render(request, 'itenerary/welcome.html', {'today': datetime.today()})