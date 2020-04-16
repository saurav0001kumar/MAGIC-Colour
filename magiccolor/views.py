from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from magiccolor.models import user
# Create your views here.
def home(request):
    return render(request,'home.html')

def magic(request):
    if request.method == 'POST':
        r=request.POST['name']
        user.save
        return render(request,'home.html',{'res':r})
    else:
        return render(request,'home.html')
