from django.urls import path
from .views import Cadastro, Login, Home


urlpatterns = [
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('login/', Login.as_view(), name='login'),
    path('home/', Home.as_view(), name='home'),
]