from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.merchantinfo_create_view, name='merchantinfo-create'),
    path('list/',views.merchantinfo_list_view, name='merchantinfo-list'),
    path('listandcreate/', views.merchant_list_create_view),
    path('rud/<int:pk>/', views.merchant_get_update_delete)  
]