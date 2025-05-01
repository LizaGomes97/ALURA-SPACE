from django.urls import path
from galeria.views import index, imagem


# lista para endpoints
urlpatterns = [
    path('',index, name = 'index'),
    path('imagem/',imagem, name = 'imagem'),
]