from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('add-blog', views.add_blog),
]
