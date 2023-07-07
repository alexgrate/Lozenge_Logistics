from django.shortcuts import render
from django.contrib import messages
from .forms import EnquiriesForm
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def aboutUs(request):
    return render(request, 'aboutUs.html', {'title': 'AboutUs'})

def Services(request):
    return render(request, 'services.html', {'title': 'Services'})

def Contact(request):
    if request.method == 'POST':
        form = EnquiriesForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            
            
            send_mail(
                'New Inquiry',
                f'Name: {first_name} {last_name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {message}',
                'alexgrate165@gmail.com',  
                ['alexgrate606@gmail.com'],  
                fail_silently=False,
            )
            messages.success(request, ('Your submission has been recieved.'))
    else:
        form = EnquiriesForm()
    return render(request, 'contact.html', {'form': form ,'title': 'Contact'})


def Faq(request):
    if request.method == 'POST':
        form = EnquiriesForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            
            
            send_mail(
                'New Inquiry',
                f'Name: {first_name} {last_name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {message}',
                'alexgrate165@gmail.com',  
                ['alexgrate606@gmail.com'],  
                fail_silently=False,
            )
            messages.success(request, ('Your submission has been recieved.'))
    else:
        form = EnquiriesForm()
    return render(request, 'faq.html', {'form': form, 'title': 'FAQ'})