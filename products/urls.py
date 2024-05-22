from django.urls import path
from . import views
# when we import a module (views) that will be used as object - views


urlpatterns = [
    path('', views.index),
    path('new', views.new)
]