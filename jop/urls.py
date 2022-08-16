
from django.urls import path
from . import views

app_name = 'jop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:id>/jop_list', views.jop_list, name='jop_list'),
    path('<int:id>', views.jop_detail, name='jop_detail'),
    path('add', views.jop_add, name='jop_add'),
    path('<str:id>/apply', views.jop_apply, name='jop_apply'),
]