from django.shortcuts import render
from .models import Jop
# Create your views here.


def jop_list(request):
    jop_list = Jop.objects.all()
    context = {'jops': jop_list}
    return render(request, 'jop/jop_list.html', context)


def jop_detail(request, id):
    jop_detail = Jop.objects.get(id = id)
    context = {'jop' : jop_detail}
    return render(request, 'jop/job_detail.html', context)