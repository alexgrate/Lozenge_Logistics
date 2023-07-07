from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('bookings/', views.Booking, name='Lozenge-bookings'),
    path('QouteForms/', views.Quotes, name='Lozenge-quoteforms'),
]