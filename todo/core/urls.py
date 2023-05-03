from django.urls import path
from . import views

urlpatterns = [
    path('',views.atividade),
    path('',views.cadastro)
]