from django import forms
from django.core.validators import RegexValidator


class EnquiriesForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'contact-input', 'placeholder': 'First Name*'}))  
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'contact-input', 'placeholder': 'Last Name*'}))  
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'contact-input', 'placeholder': 'Email*'}))
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = forms.CharField(required=True, validators=[phone_regex],widget=forms.TextInput(attrs={'class': 'contact-input', 'placeholder': 'Your Phone Number*'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'contact-input, contact-textarea', 'placeholder': 'Message*'}))
