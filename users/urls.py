from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('registrar/', views.registrar_view, name='registrar'),
    path('menu/', views.menu_view, name='menu')
]
