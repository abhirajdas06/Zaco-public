from django.shortcuts import render
from home.views import subs

# Create your views here.
def services(request):
    a = subs(request)
    return render(request,"service.html")