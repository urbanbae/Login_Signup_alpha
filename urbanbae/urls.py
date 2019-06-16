from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name="home"),
    path("", include("accounts.urls")),
]
