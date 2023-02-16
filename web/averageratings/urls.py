from django.urls import path
from . import views


urlpatterns = [
    path('listandcreate/', views.average_rating_list_create_view),
    path('update/<int:pk>/', views.average_rating_update_view),
    path('getUserDetails/', views.current_user)
]