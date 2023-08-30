from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogpost, name='blogpost'),
    path('Products/', views.products, name= 'Products')
]