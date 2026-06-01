from django.urls import path
from .views import *
from django.shortcuts import render

urlpatterns = [
    path('', home, name='home'),
    path('login/', handle_login, name='login'),
    path('signup/', handle_signup, name='signup'),
    path('logout/', handle_logout, name='logout'),
    path('product/<int:product_id>/', view_product, name='view_product'),
    path('404/', lambda request: render(request, '404.html'), name='404'),
    path('add_to_favorite/<int:product_id>/', handle_add_to_favor, name='add_to_favorite'),
    path('remove_from_favorite/<int:product_id>/', handle_remove_from_favor, name='remove_from_favorite'),
]