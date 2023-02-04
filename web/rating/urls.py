from django.urls import path
from . import views


urlpatterns = [
    path('listandcreate/', views.rating_list_create_view),
    path('rud/<int:pk>/', views.rating_get_update_delete),
    path('ratingsforuser/', views.ratings_for_user),
]