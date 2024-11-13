"""
URL configuration for pizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views  
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from models import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name='home'),
    path('login/' , views.login_view , name='login'),
    path('signup/' , views.signup_view , name='signup'),
    path('logout/' , views.logout_view , name='logout'),
    path('add_cart/<slug:pizza_id>' , views.cart , name='add_cart'),
    path('cart/' , views.cart_view , name='cart'),
    path('bin/<slug:pizza_id>' , views.bin , name='bin'),
    path('details/<slug:id>' , views.details , name='details'),
    path('homebin/<slug:pizza_id>' , views.homebin , name='homebin'),
    path('details_cart/<slug:pizza_id>' , views.details_cart , name='details_cart'),
    path('plus/<slug:id>' , views.plus , name='plus'),
    path('minus/<slug:id>' , views.minus , name='minus'),
    path('s_form/' , views.sellerform , name='s_form'),
    path('pform/' , views.pform , name='pform'),
    path('s_pizzas/' , views.s_pizzas , name='s_pizzas'),
    path('minus/<slug:id>' , views.minus , name='minus'),
    path('pizza_bin/<slug:id>' , views.pizza_bin , name='pizza_bin'),
    path('orders/' , views.orders , name='orders'),
    path('order/' , views.orderspage , name='opage'),
    path('create_order/<slug:id>' , views.create_order , name='create_order'),
]

urlpatterns+= static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
