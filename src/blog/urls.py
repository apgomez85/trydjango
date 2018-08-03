from django.urls import path
from .views import (
    blog_list_view,
    blog_detail_view,
)

app_name = 'blog'
urlpatterns = [
    path('', blog_list_view, name='blog-list'),
    path('<int:id>/', blog_detail_view, name='blog-detail'),


]
