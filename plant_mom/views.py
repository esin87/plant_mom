from django.shortcuts import render
from .models import Plant
# Create your views here.


def plants_list(request):
    plants = Plant.objects.all()
    return render(request, 'plant_mom/plants_list.html', {'plants': plants})


def plant_detail(request, pk):
    plant = Plant.objects.get(id=pk)
    return render(request, 'plant_mom/plant_detail.html', {'plant': plant})
