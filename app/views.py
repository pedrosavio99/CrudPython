from django import forms
from django.core import paginator
from django.forms.models import ModelForm
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from app.forms import MotosForm
from app.models import motos
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    
    # data = {}
    # data['moto'] = 'XTZ' #banco de dados fake so pra testar 
    data = {}
    # data['db'] = motos.objects.all()
    all = motos.objects.all()
    paginator = Paginator(all,10)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request,'index.html', data)


def form(request):
    data = {}
    data['form'] = MotosForm()
    return render(request, 'form.html', data)

def create(request):
    form = MotosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    
def edit(request,pk):
    data = {}
    data['db'] = motos.objects.get(pk=pk)
    data['form'] = MotosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = motos.objects.get(pk=pk)
    form = MotosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
    
def delete(request,pk):
    db = motos.objects.get(pk=pk)
    db.delete()
    return redirect('home')