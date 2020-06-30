from django.urls import path, include
from . import views

urlpatterns = [
    path('viewproducts/', views.productpage, name="products"),
    path('detail/<int:Products_id>', views.productdetail, name="detail")
]