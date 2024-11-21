from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
import os
# Create your views here.
def e_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['shop']=uname
                return redirect(shop_home)
            else:
                req.session['user']=uname
                return redirect(user_home)
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
    
def edit_product(req,pid):
    if req.method=='POST':
            p_id=req.POST['pid']
            name=req.POST['name']
            dis=req.POST['dis']
            price=req.POST['price']
            o_price=req.POST['o_price']
            file=req.FILES.get('img')
            if file:
                Product.objects.filter(pk=pid).update(pid=p_id,name=name,dis=dis,price=price,offer_price=o_price)
                data=Product.objects.get(pk=pid)
                data.img=file
                data.save()
            else:
                Product.objects.filter(pk=pid).update(pid=p_id,name=name,dis=dis,price=price,offer_price=o_price)
            return redirect(shop_home)
    
    else:
        data=Product.objects.get(pk=pid)
        return render(req,'shop/edit.html',{'data':data})
    
def delete_product(req,pid):
    data=Product.objects.get(pk=pid)
    file=data.img.url
    file=file.split('/')[-1]
    os.remove('media/'+file)
    data.delete()
    return redirect(shop_home)


def user_reg(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
        except:
            messages.warning(req, "email already in use")
            return redirect(user_reg)
        
        return redirect(e_login)
    else:
        return render(req,'user/register.html')

def user_home(req):
    if 'user' in req.session:
        data=Product.objects.all()
        return render(req,'user/home.html',{'products':data})
    else:
        return redirect(e_login)

def user_cart(req):
    return render(req,'user/my_cart.html')

def user_contact(req):
    return render(req,'user/contact.html')

def view_product(req,pid):
    data=Product.objects.get(pk=pid)
    return render(req,'user/view_product.html',{'product':data})

def add_to_cart(req,pid):
    product=Product.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    data=Cart.objects.create(product=product,user=user,qty=1)
    data.save()
    return redirect(view_cart)

def view_cart(req):
    return render(req,'user/cart.html')