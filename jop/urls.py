
from django.urls import path
from . import views

app_name = 'jop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:id>/jop_list', views.jop_list, name='jop_list'),
    path('my_job', views.my_job, name='my_job'),
    path('<int:id>', views.jop_detail, name='jop_detail'),
    path('add', views.jop_add, name='jop_add'),
    path('<str:id>/apply', views.jop_apply, name='jop_apply'),
    path('<str:id>/edit', views.update_job, name='jop_edit'),
    path('<str:id>/delete', views.delete_job, name='job_delete'),

]