from django.shortcuts import render

# Create your views here.
def certifications(request):
    context = {'certificates': 'active'}
    res = render(request,'cert/cert_page.html',context)
    return res
