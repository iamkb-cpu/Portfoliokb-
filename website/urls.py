from django.urls import path
from . import views
from django.urls import path
from .views import contact_view

#app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('services/', views.services_view, name='services'),
    path('about/', views.about_view, name='about'),

]


