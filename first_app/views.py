from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    my_dict = {'insert_me': 'Hello, I made this page'}
    return render(req,'index.html',context=my_dict)
def help(req):
    vpas = {'help': 'This has been redirect form help page'}
    return render(req,'help.html',context=vpas)