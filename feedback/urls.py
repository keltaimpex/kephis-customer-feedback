from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.cf, name='cf'),
    path('services/', views.services, name='services'),
    path('RATING/', views.RATING, name='RATING'),
    path('submit/', views.submit, name='submit'),
]
