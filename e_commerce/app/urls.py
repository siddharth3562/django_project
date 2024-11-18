from django.urls import path
from . import views

urlpatterns=[
    path('',views.e_login),
    path('shop_home',views.shop_home),
    path('logout',views.e_logout),
    path('add',views.add_product),
    path('edit_product/<pid>',views.edit_product)
]