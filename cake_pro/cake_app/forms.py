import datetime


from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class UserForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="confirm password")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class customerForm(forms.ModelForm):
    class Meta:
        model = customer
        exclude = ('user',)
        fields = ('Name', 'Phone_no', 'Address')


class AddcakeForm(forms.ModelForm):
    class Meta:
        model = cake
        fields = ('title', 'price', 'category', 'description', 'picture')
        widget = {
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }


class orderForm(forms.ModelForm):
    class Meta:
        model = orderplaced
        fields = ('title', 'price', 'category', 'description', 'picture')


class DateInput(forms.DateInput):
    input_type = 'date'


class payment_Form(forms.ModelForm):
    class Meta:
        model = payment
        fields = ('shipping_address', 'price', 'card_number', 'cvv', 'date')

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Invalid Date")
        return date


