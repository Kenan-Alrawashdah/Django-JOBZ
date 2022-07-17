

from django.urls import path, include
from . import views

app_name = 'jop'
urlpatterns = [
    path('', views.jop_list),
    path('<int:id>', views.jop_detail, name='jop_detail'),
]