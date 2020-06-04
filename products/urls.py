from django.urls import path, include
from . import views

urlpatterns = [
    path('viewproducts/', views.productpage, name="products"),
]