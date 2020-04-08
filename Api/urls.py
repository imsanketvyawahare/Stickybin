from django.urls import path
from . import api


urlpatterns = [
    path('', api.API.as_view())
]