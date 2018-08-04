from django.urls import path
from .views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    product_delete_view,
    product_list_view,
)

app_name = 'products'
urlpatterns = [
    path('<int:id>/', product_detail_view, name='products'),
    path('create/', product_create_view, name='create'),
    path('initial/', render_initial_data, name='initial'),
    path('<int:id>/delete/', product_delete_view, name='delete'),
    path('', product_list_view, name='list'),


]
