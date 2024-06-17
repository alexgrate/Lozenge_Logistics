from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegisterForm, BookingForms, QuotesForms
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your account has been created! You are now able to log in'))
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'title': 'SignUp', 'form': form})



def logout_user(request):
    logout(request)
    messages.success(request, ('You Were Logged Out!'))
    return redirect('login')

@login_required
def Booking(request):
    if request.method == 'POST':
        form = BookingForms(request.POST)
        if form.is_valid():
            Shipping_Opt = form.cleaned_data['Shipping_opt']
            Sender_Fname = form.cleaned_data['Sender_Fname']
            Sender_Lname = form.cleaned_data['Sender_Lname']
            Sender_Address = form.cleaned_data['Sender_Address']
            Sender_Phone = form.cleaned_data['Sender_Phone']
            Sender_Email = form.cleaned_data['Sender_Email']
            Reciever_Fname = form.cleaned_data['Reciever_Fname']
            Reciever_Lname = form.cleaned_data['Reciever_Lname']
            Reciever_Phone = form.cleaned_data['Reciever_Phone']
            Reciever_Email = form.cleaned_data['Reciever_Email']
            Reciever_Address = form.cleaned_data['Reciever_Address']
            Reciever_City = form.cleaned_data['Reciever_City']
            Reciever_State = form.cleaned_data['Reciever_State']
            Reciever_Countries = form.cleaned_data['Reciever_Countries']
            Product_List = form.cleaned_data['Product_List']
            Insurance_opt = form.cleaned_data['Insurance_opt']
            
            send_mail(
                'New Bookings',
                f'Shipping-Option: {Shipping_Opt}\nSender-FirstName: {Sender_Fname}\nSender-LastName: {Sender_Lname}\nSender-Address: {Sender_Address}\nSender-Phone: {Sender_Phone}\nSender-Email: {Sender_Email}\nReciever-FirstName: {Reciever_Fname}\nReciever-LastName: {Reciever_Lname}\nReciever-Phone: {Reciever_Phone}\nReciever-Email: {Reciever_Email}\nReciever-Address: {Reciever_Address}\nReciever-City: {Reciever_City}\nReciever-State: {Reciever_State}\nReciever-Country: {Reciever_Countries}\nProduct-List: {Product_List}\nInsurance-Option: {Insurance_opt}',
                'alexgrate165@gmail.com',  
                ['alexgrate606@gmail.com'],  
                fail_silently=False,
            )
            messages.success(request, ('Your submission has been recieved.'))
    else:
        form = BookingForms()
    return render(request, 'bookings.html', {'form': form, 'title': 'Bookings'})

def Quotes(request):
    if request.method == 'POST':
        form = QuotesForms(request.POST)
        if form.is_valid():
            Origin = form.cleaned_data['Origin']
            Destination = form.cleaned_data['Destination']
            Estimated_Weight = form.cleaned_data['Estimated_Weight']
            Email = form.cleaned_data['Email']
            Phone = form.cleaned_data['Phone']
            
            send_mail(                
                'New Quote Form',
                f'Origin: {Origin}\nDestination: {Destination}\nEstimated_weight: {Estimated_Weight}\nEmail: {Email}\nPhone: {Phone}',
                'alexgrate165@gmail.com',  
                ['alexgrate606@gmail.com'],  
                fail_silently=False,
            )
            messages.success(request, ('Your quote request has been submitted successfully!'))
    else:
        form = QuotesForms()
    return render(request, 'quote.html', {'form': form, 'title': 'Quotes'})