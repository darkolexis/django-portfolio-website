from django.shortcuts import render

# Create your views here.
def education(request):
    context = {'education': 'active'}
    res = render(request,'education/edu.html',context)
    return res
