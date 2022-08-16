from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.send_massage, name='contact'),
    path('about_us', views.about_us, name='about_us')
]
