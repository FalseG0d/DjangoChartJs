from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home),
    path('sales-chart', views.pie_chart, name='sales-chart'),
]