from django.urls import path
from . import views

urlpatterns=[
    path('',views.e_login),
    path('shop_home',views.shop_home),
    path('logout',views.e_logout),
    path('add',views.add_product),
    path('edit_product/<pid>',views.edit_product),
    path('delete_product/<pid>',views.delete_product),
    path('view_bookings',views.view_bookings),

    path('user_home',views.user_home),
    path('user_reg',views.user_reg),
    path('user_contact',views.user_contact),
    path('view_product/<pid>',views.view_product),
    path('view_cart',views.view_cart),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('qty_in/<cid>',views.qty_in),
    path('qty_dec/<cid>',views.qty_dec),
    path('cart_pro_buy/<cid>',views.cart_pro_buy),
    path('bookings',views.bookings),
    path('pro_buy/<pid>',views.pro_buy),
]