from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clerk/', views.clerk, name='clerk'),
    path('clerk/register2',views.register2, name='register2'),
    path('clerk/model_form_upload',views.model_form_upload, name='model_form_upload'),
    path('booking',views.booking, name='booking'),
    path('clerk/checkout',views.checkout, name='checkout'),
    path('clerk/checkoutProceed',views.checkoutProceed, name='checkoutProceed'),
    path('clerk/checkin',views.checkin, name='checkin'),
]
