from .models import Employee
from django.shortcuts import render
from .custom_views.Employee import *
from .custom_views.Address import *
from .custom_views.Client import *
from .custom_views.Service import *
from .custom_views.Item import *
from .custom_views.Service_Order import *

def index(request):
    shelf = Employee.objects.all()
    return render(request, 'work/index.html',
                  {'shelf': shelf})