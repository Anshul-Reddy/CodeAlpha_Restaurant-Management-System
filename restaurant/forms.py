from datetime import date
from django.contrib.admin import widgets
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["customer_name","customer_email","date","time",]

        widgets={
            "cutomer_name":forms.TextInput(attrs={"placeholder":"Enter Your Name"}),
            "customer_email":forms.TextInput(attrs={"placeholder":"Enter Your Email"}),
            "date": forms.DateInput(attrs={"type":"date"}),
            "time": forms.TimeInput(attrs={"type":"time"}), 
        }