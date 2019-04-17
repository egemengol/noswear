
from django.urls import path, include

from . import views

urlpatterns = [
    path('json/<in_text>/', views.out_json, name="out_json"),
    path('plain/<in_text>/', views.out_plain, name="out_plain"),
]
