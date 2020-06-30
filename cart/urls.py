from django.urls import path, include
from cart import views


urlpatterns = [
    path('view/', views.view_cart, name="view_cart"),
    path('add/<id>', views.add_to_cart, name="add_to_cart"),
    path('adjust/<id>', views.adjust_cart, name="adjust_cart"),
]