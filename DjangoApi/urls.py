"""
URL configuration for DjangoApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from api.login.login_view import( login_view,
register_view,forgot_login_view,logout_view,)

from api.home.home_view import (home_view,home_shop,home_about,home_services,
                                home_blog,home_contact,home_cart,home_checkout,
                                home_thankyou)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/', login_view, name = "index"),
    
    path('logout/', logout_view, name = "logout"),
    
    path('register/', register_view, name = "register"),
    path('forgot_password/', forgot_login_view, name = "forgot_password"),
    
    
    path('', home_view, name = "home"),
    path('home/', home_view, name = "home"),
    path('shop/', home_shop, name = "shop"),

    path('about/', home_about, name = "about"),
    path('services/', home_services, name = "services"),
    path('blog/', home_blog, name = "blog"),
    path('contact/', home_contact, name = "contact"),
    path('cart/', home_cart, name = "cart"),
    path('checkout/', home_checkout, name = "checkout"),
    path('thankyou/', home_thankyou, name = "thankyou"),


]
