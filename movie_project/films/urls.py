from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_movie/', views.add_movie, name='page2'),
]