from django.urls import path
from . import views


urlpatterns = [
    path('listandcreate/', views.cart_list_create_view),
    path('rud/<int:pk>/', views.cart_get_update_delete),
    path('custom/', views.cart_custom_view)
]