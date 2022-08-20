from django.urls import path
from .views import PaginaPerfil

app_name = 'usuarios'
urlpatterns = [
    path('perfil', PaginaPerfil.as_view() , name="perfil" )
]
