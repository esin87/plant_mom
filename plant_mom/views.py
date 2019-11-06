from django.shortcuts import render, redirect
from .models import Plant
from .forms import PlantForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def plants_list(request):
    plants = Plant.objects.all()
    return render(request, 'plant_mom/plants_list.html', {'plants': plants})


def plant_detail(request, pk):
    plant = Plant.objects.get(id=pk)
    return render(request, 'plant_mom/plant_detail.html', {'plant': plant})


@login_required
def plant_create(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            plant = form.save()
            return redirect('plant_detail', pk=plant.pk)
    else:
        form = PlantForm()
    return render(request, 'plant_mom/plants_create.html', {'form': form})


@login_required
def plant_edit(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == "POST":
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            plant = form.save()
            return redirect('plant_detail', pk=plant.pk)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plant_mom/plants_create.html', {'form': form})


@login_required
def plant_delete(request, pk):
    Plant.objects.get(id=pk).delete()
    return redirect('plants_list')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('plants_list')
    else:
        form = UserCreationForm()
    return render(request, 'plant_mom/signup.html', {'form': form})
