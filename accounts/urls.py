from django.urls import path, include
from accounts import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('account/', views.account, name="account"),
    path('update/<int:Order_id>', views.updatestatus, name="statusupdate"),
    path('addnews', views.addnewsitem, name='addnews'),
]