from django.urls import path
from galeria.views import index

# lista para endpoints
urlpatterns = [
    path('',index),
]