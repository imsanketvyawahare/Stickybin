from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('<str:code>/', views.display, name="display"),
    path('api', views.api, name="api"),
]