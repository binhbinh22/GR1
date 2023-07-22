from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views
urlpatterns =[
    path('', views.index),
    path('contact/', views.contact),
    path('model/', views.model)
    #path('login/', auth_views.login, {'template_name': 'page/login.html'})
]