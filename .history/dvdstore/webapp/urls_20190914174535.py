from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clerk/', views.clerk, name='clerk'),
    path('clerk/register2',views.register2, name='register2'),
    path('clerk/register3',views.register3, name='register3'),
    path('clerk/model_form_upload',views.model_form_upload, name='model_form_upload'),
    
    path('transactions/register2',views.register2, name='register2'),
    path('transactions/register3',views.register3, name='register3'),
    path('transactions/model_form_upload',views.model_form_upload, name='model_form_upload'),
    
    path('booking',views.booking, name='booking'),
    path('clerk/checkout',views.checkout, name='checkout'),
    path('clerk/checkin',views.checkin, name='checkin'),
    path('transactions/', views.transactions, name='transactions'),
    path('userstbl/', views.userstbl, name='userstbl'),
    path('transactions/register2',views.register2, name='register2'),
    path('transactions/register3',views.register3, name='register3'),
    path('transactions/model_form_upload',views.model_form_upload, name='model_form_upload'),


    path('clerk/deleteMovie',views.deleteMovie, name='deleteMovie'),
    path('transactions/deleteTransaction',views.deleteTransaction, name='deleteTransaction'),

    path('userstbl/deleteUser',views.deleteUser, name='deleteUser'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('accounts/registerCustomer',views.registerCustomer, name='registerCustomer'),
    path('user_detail/updateCustomer',views.updateCustomer, name='updateCustomer'),
    path('user_detail/updateUser',views.updateUser, name='updateUser'),



    
]
