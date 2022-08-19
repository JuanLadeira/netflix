from django.urls import path
from .views import templateview

app_name = 'usuarios'
urlpatterns = [
    path('usuario', templateview , name="usuario" )
]
