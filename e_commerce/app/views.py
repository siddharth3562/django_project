from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def e_login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            return redirect(shop_home)
        else:
            return redirect(e_login)
    else:
        messages.warning(req, "Your account expires in three days.")

        return render(req,'login.html')
    
def shop_home(req):
    return render(req,'shop/home.html')