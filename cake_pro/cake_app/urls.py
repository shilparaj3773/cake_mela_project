from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admhome/', views.admhome, name='admhome'),
    path('login/', views.login, name='login'),
    path('userview/', views.userview, name='userview'),
    path('signup/', views.signup, name='signup'),
    path('signup1/', views.signup1, name='signup1'),
    path('cxhome/', views.cxhome, name='cxhome'),
    path('makerhome/', views.makerhome, name='makerhome'),
    path('add_cake/', views.add_cake, name='add_cake'),
    path('update_cake/<int:id>/', views.update_cake, name='update_cake'),
    path('viewcake/', views.viewcake, name='viewcake'),
    path('viewcakess/', views.viewcakess, name='viewcakess'),
    path('view_customers/', views.view_customers, name='view_customers'),
    path('view_maker/', views.view_maker, name='view_maker'),
    path('update_customer/<int:id>/', views.update_customer, name='update_customer'),
    path('delete_cake/<int:id>/', views.delete_cake, name='delete_cake'),
    path('view_cake', views.view_cake, name='view_cake'),
    path('view_order', views.view_order, name='view_order'),
    path('add_order/<int:id>/', views.add_order, name='add_order'),
    path('view_cake_order', views.view_cake_order, name='view_cake_order'),
    path('confirm_order/<int:id>/', views.confirm_order, name='confirm_order'),
    path('rej_order/<int:id>/', views.rej_order, name='rej_order'),
    path('delete_order/<int:id>/', views.delete_order, name='delete_order'),
    path('payments/<int:id>/', views.payments, name='payments'),
    path('view_adm_cake/', views.view_adm_cake, name='view_adm_cake'),


]
