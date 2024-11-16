from django import forms
from .models import *
import re
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {'password': forms.PasswordInput}
        help_texts = {'password': 'password must contain 1 number (0-9), password must contain 1 uppercase letters, password must contain 1 lowercase letters, password must contain 1 non-alpha numeric number, password is 8-16 characters with no space'}
    def clean_password(self):
        pw = self.cleaned_data.get('password')
        if re.match(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$', pw):
            return pw
        raise forms.ValidationError('invalid Password')
    
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
    
