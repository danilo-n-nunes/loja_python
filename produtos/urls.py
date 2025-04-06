from django.urls import path
from .views import lista_produtos, adicionar_produto, editar_produto, excluir_produto

urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('adicionar/', adicionar_produto, name='adicionar_produto'),
    path('editar/<int:pk>/', editar_produto, name='editar_produto'),
    path('excluir/<int:pk>', excluir_produto, name='excluir_produto'),
]
