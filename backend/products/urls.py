from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.product_create_view, name='product-create'),
    path('list/',views.product_list_view, name='product-list'),
    path('detail/<int:pk>/',views.product_detail_view, name='product-detail'),
    path('destroy/<int:pk>/',views.product_destroy_view, name='product-destroy'),
    path('update/<int:pk>/',views.product_update_view, name='product-update'),

]