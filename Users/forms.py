from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django_countries.fields import CountryField



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password Confirmation'


SHIPPING_OPTION = (
    ('A', 'ARAMEX'),
    ('D', 'DHL'),
    ('F', 'FEDEX'),
    ('U', 'UPS'),
)

INSURANCE_OPTION = (
    ('YES', 'I want Insurance'),
    ('NO', 'I do not want Insurance'),
)


class BookingForms(forms.Form):
    Shipping_opt = forms.ChoiceField(required=True, choices=SHIPPING_OPTION, widget=forms.RadioSelect)
    Sender_Fname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First name'}))  
    Sender_Lname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    Sender_Address = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Input your address'}))    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    Sender_Phone = forms.CharField(required=True, validators=[phone_regex],widget=forms.TextInput(attrs={'placeholder': 'Input your phone number'}))
    Sender_Email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Input your email'}))
    Reciever_Fname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First name'}))  
    Reciever_Lname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    Reciever_Phone = forms.CharField(required=True, validators=[phone_regex],widget=forms.TextInput(attrs={'placeholder': "Input reciever's phone number"}))
    Reciever_Email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': "Input reciever's email"}))
    Reciever_Address = forms.CharField(required=True, widget=forms.TextInput(attrs={'required': 'required'}))    
    Reciever_City = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    Reciever_State = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'State / Province / Region'}))
    Reciever_Countries = CountryField(blank_label='Select Country').formfield()
    Product_List = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Name: Wigs Quantity: 10 packs Unit Price: 40,000'}))
    Checkbox01 = forms.BooleanField(label='I hereby declare that I am the Shipper of the aforementioned items and certify that I have not hidden or attempted to hide any other item in my shipment. I affirm that the provided list accurately represents all the items that I am shipping.', required=True)
    Checkbox02 = forms.BooleanField(label='I acknowledge that trying to export illegal or prohibited items may result in severe legal consequences, including the possibility of being caught, prosecuted, and potentially being forced to pay a fine or face other penalties. Therefore, I understand that it is crucial to follow all applicable laws and regulations related to exporting goods to avoid any negative outcomes.', required=True)
    Checkbox03 = forms.BooleanField(label='If Lozenge Logistics finds out that I have not disclosed any item that is not listed above and have provided false information, they will not ship the items or the entire shipment. In case the shipment has already been shipped, I will be held accountable for all the expenses incurred by Lozenge Logistics in retrieving, destroying, or reshipping the item(s) as required by law.', required=True)
    Checkbox04 = forms.BooleanField(label='I have provided a valid ID and Contact Address where I can be reached at all times.', required=True)
    Checkbox05 = forms.BooleanField(label='I acknowledge that I may be subject to Duty charges imposed by the Customs authorities of the receiving country. If such charges arise, DHL/UPS will inform me accordingly using different terminology.', required=True)
    Insurance_opt = forms.ChoiceField(required=True, choices=INSURANCE_OPTION, widget=forms.RadioSelect)


class QuotesForms(forms.Form):
    Origin = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': 'Nigeria'}))
    Destination = forms.CharField(required=True)
    Estimated_Weight = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    Phone = forms.CharField(required=True, validators=[phone_regex])

    
    