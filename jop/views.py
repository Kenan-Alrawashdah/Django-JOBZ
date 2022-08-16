from audioop import reverse
from distutils.log import debug
from unicodedata import category
from django.shortcuts import redirect, render
from .models import Category, Jop
from django.core.paginator import Paginator
from .form import ApplyForm, JopForm
from .filter import JopFilter
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'jop/index.html', context)


def jop_list(request, id):
    categories_id = Category.objects.get(id=id)
    jop_list = Jop.objects.filter(category=categories_id)
    #jop_list = Jop.objects.all()
    categories = Category.objects.all()
    filter_list = JopFilter(request.GET, queryset= jop_list)
    jop_list = filter_list.qs
    paginator = Paginator(jop_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jops': page_obj, 'categories': categories, 'filter': filter_list}
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
            return redirect('jops:index')

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
            return redirect('jops:jop_list', id= id)

    else:
        form = ApplyForm()
    
    context = {'form': form}
    return render(request, 'jop/jop_apply.html', context)         



