from rest_framework import generics
from .models import Rating
from .serializers import RatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication

# Create your views here.


class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
    
rating_list_create_view = RatingListCreateView.as_view()

class RatingGetUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    lookup_field = 'pk'
    serializer_class = RatingSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
    
rating_get_update_delete = RatingGetUpdateDeleteView.as_view()    