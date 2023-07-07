from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Lozenge-home'),
    path('aboutUs/', views.aboutUs, name='Lozenge-aboutUs'),
    path('services/', views.Services, name='Lozenge-services'),
    path('contact/', views.Contact, name='Lozenge-contact'),
    path('FrequentlyAskedQuestions/', views.Faq, name='Lozenge-FAQ'),
]