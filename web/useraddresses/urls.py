from django.urls import path
from . import views


urlpatterns = [
    path('listandcreate/', views.address_list_create_view),
    path('rud/<int:pk>/', views.address_get_update_delete),
]