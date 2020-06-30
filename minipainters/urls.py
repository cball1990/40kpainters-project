from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.home, name='home'),
    #accounts
    path('accounts/', include('accounts.urls')),
    #products
    path('product/', include('products.urls')),
    #cart
    path('cart/', include('cart.urls')),
    #order
    path('order/', include('order.urls')),
    #gallery
    path('gallery/', include('gallery.urls')),
    #reviews
    path('review/', include('review.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
