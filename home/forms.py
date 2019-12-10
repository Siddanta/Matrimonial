from .models import enquiry
from django import forms

class enquiries(forms.ModelForm):

    class Meta:
        model = enquiry
        fields = ('Email','Enquiry')
