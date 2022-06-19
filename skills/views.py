from django.shortcuts import render

# Create your views here.
def myskills(request):
    context = {'skills': 'active'}
    res = render(request,'skills/myskills.html',context)
    return res
