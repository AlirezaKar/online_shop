from django.urls import path
from .views import index, shopping_basket_view, product_detail_view, add_to_list

urlpatterns = [
    path('', index, name='index'),
    path('basket/', shopping_basket_view, name='shopping_basket_view'),
    path('<int:id>', product_detail_view, name='product_detail_view'),
    path('<int:id>/add_count', add_to_list, name='add_to_list'),
    

]