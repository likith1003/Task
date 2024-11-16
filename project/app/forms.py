from django import forms
from .models import *
import re
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {'password': forms.PasswordInput}
class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        exclude = ['username']
        roles = [('Owner', 'Owner'),
                ('Director', 'Director'),
                ('Finance Manager','Finance Manager'),
                ('General Manager', 'General Manager')
        ]
        widgets = {'Role': forms.Select(choices=roles)}

    def clean_Contact_Number(self):
        Contact_no = self.cleaned_data.get('Contact_Number')
        if re.match('^(\+91|\+91\-|0)? ?[789]\d{9}$', Contact_no):
            return Contact_no
        raise forms.ValidationError('Please enter a valif phone number')

    def clean_Whatsapp_Number(self):
        Whatsapp_no = self.cleaned_data.get('Contact_Number')
        if re.match('^(\+91|\+91\-|0)? ?[789]\d{9}$', Whatsapp_no):
            return Whatsapp_no
        raise forms.ValidationError('Please enter a valif phone number')
    