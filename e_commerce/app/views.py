from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
# Create your views here.
def e_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['shop']=uname
            return redirect(shop_home)
        else:
            messages.warning(req, "invalid username or password")
            return redirect(e_login)
    else:
        return render(req,'login.html')
    
def shop_home(req):
    return render(req,'shop/home.html')

def e_logout(req):
    logout(req)
    req.session.flush()
    return redirect(e_login)

def shop_home(req):
    if 'shop' in req.session:
        data=Product.objects.all()
        return render(req,'shop/home.html',{'products':data})
    else:
        return redirect(e_login)
    
def add_product(req):
    if 'shop' in req.session:
        if req.method=='POST':
            pid=req.POST['pid']
            name=req.POST['name']
            dis=req.POST['dis']
            price=req.POST['price']
            o_price=req.POST['o_price']
            file=req.FILES['img']
            data=Product.objects.create(pid=pid,name=name,dis=dis,price=price,offer_price=o_price,img=file)
            data.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/add_pro.html')
    else:
        return redirect(e_login)