from django import forms
from .models import DVD, Customer

class DocumentForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = ('Title','year','genre','InStock','Synopsis','BookingPickup' ,'NumOfTimesRented','ImageDVD')


class customerForm:
    class Meta:
        model= Customer
        #user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)

        fields = ('username','password,'phone_number','address','identification')

