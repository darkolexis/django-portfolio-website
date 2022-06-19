from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    context = {'home': 'active'}
    res = render(request,'core/home.html',context)
    return res

def contact(request):
    context = {'contact': 'active'}
    res = render(request,'core/contact.html',context)
    return res
