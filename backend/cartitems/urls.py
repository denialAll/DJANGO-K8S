from django.urls import path
from . import views


urlpatterns = [
    path('listandcreate/', views.cart_item_list_create_view),
    path('rud/<int:pk>/', views.cart_item_get_update_delete),
    path('newitemlist/', views.new_cart_item_list),
    path('accepteditemlist/', views.accepted_cart_item_list),
    path('newandacceptedlist/', views.new_accepted_cart_item_list)
]