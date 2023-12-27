from django.shortcuts import render

from app.models import *

# Create your views here.

def forms(request):
    if request.method =='POST':
        Name=request.POST['na']
        password=request.POST['ps']
        mail=request.POST['ma']
        phono=request.POST['no']

        ob=jsp.objects.get_or_create(Name=Name,password=password,mail=mail,phno=phono)[0]
        ob.save()

        







    return render(request,'forms.html')
