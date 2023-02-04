from django.urls import path
from . import views

urlpatterns = [
    path('listandcreate/', views.image_list_create_view)
]