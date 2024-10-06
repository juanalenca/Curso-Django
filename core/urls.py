from django.urls import path  # Importa a função 'path' para definir as URLs do app

from .views import index, contato  # Importa as views 'index' e 'contato' do arquivo views.py

# Define a lista de URLs (roteamento do app)
urlpatterns = [
    path('', index),
    path('contato', contato)
]
