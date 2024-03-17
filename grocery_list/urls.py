from django.urls import path
from .views import item_create, item_update, item_delete, lista, search_view, on_cart, hide_items

urlpatterns = [
    path('', lista, name='item_lista'),
    path('search/', search_view, name='search_view'),
    path('novo/', item_create, name='item_create'),
    path('update/<uuid:id>/', item_update, name='item_update'),
    path('delete/<uuid:id>/', item_delete, name='item_delete'),
    path('on_cart/<uuid:id>/', on_cart, name='on_cart'),
    path('hide_items/', hide_items, name='hide_items'),
]

