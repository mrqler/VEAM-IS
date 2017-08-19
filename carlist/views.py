from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloVEAM(request):
    my_dict = {
        'insert_me':"Hello I am from views.py of carlist apps",

    }
    return render(request,'index.html',context=my_dict)

def helpVeam(request):
    help_dict = {
        'insert_help':"Hello I am from views.py, I am here for helping you"
    }
    return render(request,'help.html',context=help_dict)
