from django.urls import path
from .views import nome_create, nome_update, nome_delete, lista, search_view

urlpatterns = [
    path('', lista, name='nome_lista'),
    path('search/', search_view, name='search_view'),
    path('novo/', nome_create, name='nome_create'),
    path('update/<uuid:id>/', nome_update, name='nome_update'),
    path('delete/<uuid:id>/', nome_delete, name='nome_delete'),
]
