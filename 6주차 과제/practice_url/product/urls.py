
from product import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.productlist),
    path('first/',views.productfirst)
]