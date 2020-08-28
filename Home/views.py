from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

def Home(request):
    return render(request,'index.html')


def pie_chart(request):
    labels = []
    data = []

    queryset = Sales.objects.order_by('-sales')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })