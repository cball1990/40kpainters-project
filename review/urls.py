from django.urls import path, include
from . import views

urlpatterns = [
    path('add_review', views.add_review, name="add_review"),
    path('reviews', views.reviews, name="reviews"),
]