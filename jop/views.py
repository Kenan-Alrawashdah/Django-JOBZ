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
    jobs = Jop.objects.all().order_by('-published_at')[:5]
    context = {'categories':categories, 'jobs':jobs}
    return render(request, 'jop/index.html', context)


def jop_list(request, id):
    if id == "0":
        jop_list = Jop.objects.all()
    else :
        categories_id = Category.objects.get(id=id)
        jop_list = Jop.objects.filter(category=categories_id)
        
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
            return redirect('jops:my_job')

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
    
    context = {'form': form, 'id':id}
    return render(request, 'jop/jop_apply.html', context)         


@login_required
def my_job(request):
    user = request.user
    jop_list = Jop.objects.filter(user=user)
    categories = Category.objects.all()
    filter_list = JopFilter(request.GET, queryset= jop_list)
    jop_list = filter_list.qs
    paginator = Paginator(jop_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jops': page_obj, 'categories': categories, 'filter': filter_list}
    return render(request, 'jop/my_job.html', context)


def update_job(request, id):
    job = Jop.objects.get(id=id)
    
    if request.method == "POST":
        jobform = JopForm(request.POST, request.FILES, instance=job)
        if jobform.is_valid:
            myjobform = jobform.save(commit=False)
            myjobform.user = request.user
            myjobform.save()
            return redirect('/jops/my_job')
    else :
        jobform = JopForm(instance=job)
    return render(request, 'jop/job_edit.html',{'jobform': jobform})    


def delete_job(request, id):
    jop = Jop.objects.get(id= id)

    if request.method == "POST":
        jop.delete()
        return redirect('/jops/my_job')
    
    return render(request, 'jop/job_delete.html', {'jop': jop})


