from django.urls import path
from . import views


urlpatterns = [
    path('listandcreate/', views.cart_item_list_create_view),
    path('rud/<int:pk>/', views.cart_item_get_update_delete),
]