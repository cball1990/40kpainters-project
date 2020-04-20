from django.urls import path, include
from . import views

urlpatterns = [
    path('add_review', views.addreview, name="addreview"),
    path('reviews', views.reviews, name="reviews"),
]