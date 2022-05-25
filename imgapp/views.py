#from multiprocessing import context
import os
from django.shortcuts import render,redirect
from .models import UserProfile

# Create your views here.


def load_profile_page(request):
    return render(request,'register.html')

def add_profile(request):
    if request.method == 'POST':
        uname=request.POST['name']
        uemail=request.POST['email']
        #image=request.FILES.get('file')
        if request.FILES.get('file') is not None:
            image = request.FILES['file']
        else:
            image = "/static/image/default.png"
        userPrfl = UserProfile(name=uname,email=uemail,image=image)
        print("save")
        userPrfl.save()
        return redirect('show_details')
    return render(request,'register.html')

def show_details(request):
    user_data = UserProfile.objects.all()
    return render(request,'table.html',{'user_data':user_data})

def edit_user_page(request,pk):
    udata=UserProfile.objects.get(id=pk)
    return render(request,'edit.html',{'udata':udata})

def edit_user_data(request,pk):
    if request.method=='POST':
        userdatas = UserProfile.objects.get(id=pk)
        userdatas.name = request.POST.get('name')
        userdatas.email = request.POST.get('email')
        if request.FILES.get('file') is not None:
            if not userdatas.image == "/static/image/default.png":
                os.remove(userdatas.image.path)
                userdatas.image = request.FILES['file']
            else:
                userdatas.image = request.FILES['file']
        else:
            os.remove(userdatas.image.path)
            userdatas.image = "/static/image/default.png" 
        userdatas.save()
        return redirect('show_details')
    return render(request, 'edit.html')


def delete_user_data(request,pk):
    udatas=UserProfile.objects.get(id=pk)
    if udatas.image is not None:
        if not udatas.image == "/static/image/default.png":
            os.remove(udatas.image.path)
        else:
            pass
    udatas.delete()
    return redirect('show_details')
