from django.db.models.fields import IPAddressField
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Participante
from .models import Conferencista

# Create your views here.

def index(request):
    return render(request, 'app_conferencias/index.html')

def participantes(request):
    if request.method == 'POST':
        nombre  = request.POST.get('nombre')
        apellido  = request.POST.get('apellido')
        correo  = request.POST.get('correo')
        twitter  = request.POST.get('twitter')

        p = Participante(nombre=nombre, apellido=apellido, correo=correo, twitter=twitter)
        p.save()

        messages.add_message(request, messages.INFO, f'El participante {nombre} {apellido} ha sido agregado con exito')

    q = request.GET.get('q')

    if q:

        data = Participante.objects.filter(nombre__startswith=q).order_by('nombre')
    else: 

        data = Participante.objects.all().order_by('nombre')

    ctx = {
        'formulario': data,
        'q':q
    }

    return render(request, 'app_conferencias/participantes.html', ctx)

def conferencistas(request):
    if request.method == 'POST':
        nombre  = request.POST.get('nombre')
        apellido  = request.POST.get('apellido')
        experiencia  = request.POST.get('experiencia')

        c = Conferencista(nombre=nombre, apellido=apellido, experiencia=experiencia)
        c.save()
        
        messages.add_message(request, messages.INFO, f'El conferencista {nombre} {apellido} ha sido agregado con exito')
    
    q = request.GET.get('q')

    if q:

        data = Conferencista.objects.filter(nombre__startswith=q).order_by('nombre')
    else: 

        data = Conferencista.objects.all().order_by('nombre')

    ctx = {
        'formulario': data,
        'q':q
    }

    return render(request, 'app_conferencias/conferencistas.html', ctx)

