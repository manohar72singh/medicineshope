from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.profile),
    path('index', views.index),
    path('viewMedicine/',views.viewMedicine),
    path('viewCustomer/',views.viewCustomer),
    path('addNewCustomer/',views.addNewCustomer),
    path('addNewMedicine/',views.addNewMedicine),
]