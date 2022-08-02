from audioop import reverse
from distutils.log import debug
from django.shortcuts import redirect, render
from .models import Category, Jop
from django.core.paginator import Paginator
from .form import ApplyForm, JopForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def get_categories(request):
    get_categories = Category.objects.all()
    context = {'categories': get_categories}
    return render(request, 'jop/jop_list.html', context)

def jop_list(request):
    jop_list = Jop.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(jop_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jops': page_obj, 'categories': categories}
    return render(request, 'jop/jop_list.html', context)


def jop_detail(request, id):
     jop_detail = Jop.objects.get(id = id)
     context = {'jop' : jop_detail}
     return render(request, 'jop/job_detail.html', context)

@login_required
def jop_add(request):

    if request.method == 'POST':
        form = JopForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('jops:jop_list')

    else:
        form = JopForm()
    
    context = {'form': form}
    return render(request, 'jop/jop_add.html', context)     

@login_required
def jop_apply(request, id):
    print('============================================'+id)
    jop = Jop.objects.get(id = id)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.jop = jop
            myform.save()
            return redirect('jops:jop_list')

    else:
        form = ApplyForm()
    
    context = {'form': form}
    return render(request, 'jop/jop_apply.html', context)         



