from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .models import Plantas, Tierras, Macetas
from .forms import PlantasForm, MacetasForm, TierrasForm


# Create your views here.

def home(request):

    plantas = Plantas.objects.all()
    tierras = Tierras.objects.all()
    macetas = Macetas.objects.all()
    data = {
        'plantas': plantas,
        'tierras': tierras,
        'macetas': macetas,
    }
    return render(request, 'prueba/index.html', data)

def plantas(request):

    plantas = Plantas.objects.all()
    data = {
        'plantas': plantas
    }
    
    return render(request, 'prueba/plantas.html', data)


def tierras(request):

    tierras = Tierras.objects.all()
    data = {
        'tierras': tierras
    }
    
    return render(request, 'prueba/tierras.html', data)

def macetas(request):

    macetas = Macetas.objects.all()
    data = {
        'macetas': macetas
    }
    
    return render(request, 'prueba/macetas.html', data)

def jaja(request):
    return render(request, 'prueba/jaja.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)

def agregar(request):  

    data = {
        'form': PlantasForm()
    }

    if request.method == 'POST': 
        formulario = PlantasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

            data["mensaje"] = "guardado correctamente"

    return render(request, 'producto/agregar.html', data)

def agregar2(request):  

    data = {
        'form': MacetasForm()
    }

    if request.method == 'POST': 
        formulario = MacetasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

            data["mensaje"] = "guardado correctamente"

    return render(request, 'producto/agregar2.html', data)

def agregar3(request):  

    data = {
        'form': TierrasForm()
    }

    if request.method == 'POST': 
        formulario = TierrasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

            data["mensaje"] = "guardado correctamente"

    return render(request, 'producto/agregar3.html', data)


def listar(request):

    plantas = Plantas.objects.all()
    tierras = Tierras.objects.all()
    macetas = Macetas.objects.all()
    data = {
        'plantas': plantas,
        'tierras': tierras,
        'macetas': macetas,
    }

    return render(request, 'producto/listar.html', data)


def modificar(request, id):

    plantas = get_object_or_404(Plantas, id=id)

    data = {
        'form': PlantasForm(instance=plantas)
    }

    if request.method == 'POST':
        formulario = PlantasForm(data=request.POST, instance=plantas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar")
        data["form"] = formulario

    return render(request, 'producto/modificar.html', data)


def modificar2(request, id):

    macetas = get_object_or_404(Macetas, id=id)

    data = {
        'form': MacetasForm(instance=macetas)
    }

    if request.method == 'POST':
        formulario = MacetasForm(data=request.POST, instance=macetas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar")
        data["form"] = formulario

    return render(request, 'producto/modificar2.html', data)

def modificar3(request, id):

    tierras = get_object_or_404(Tierras, id=id)

    data = {
        'form': TierrasForm(instance=tierras)
    }

    if request.method == 'POST':
        formulario = TierrasForm(data=request.POST, instance=tierras, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar")
        data["form"] = formulario

    return render(request, 'producto/modificar3.html', data)


def eliminar(request, id):

    plantas = get_object_or_404(Plantas, id=id)
    plantas.delete()
    
    return redirect(to="listar")

def eliminar2(request, id):

    macetas = get_object_or_404(Macetas, id=id)
    macetas.delete()
    
    return redirect(to="listar")

def eliminar3(request, id):

    tierras = get_object_or_404(Tierras, id=id)
    tierras.delete()
    
    return redirect(to="listar")