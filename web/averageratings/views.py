from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import AverageRating
from .serializers import AverageRatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from decimal import Decimal

# Create your views here.


class AverageRatingListCreateView(generics.ListCreateAPIView):
    queryset = AverageRating.objects.all()
    serializer_class = AverageRatingSerializer
    authentication_classes = ( TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(customer = self.request.user)

average_rating_list_create_view = AverageRatingListCreateView.as_view()

class AverageRatingUpdateView(generics.UpdateAPIView):
    queryset = AverageRating.objects.all()
    lookup_field = 'pk'
    serializer_class = AverageRatingSerializer
    authentication_classes = ( TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def patch(self,request, pk):

        rating_obj = AverageRating.objects.get(pk=pk)
        data = request.data
        print(data["taste"])
        rating_obj.taste = ((rating_obj.taste * rating_obj.orders) + Decimal(data["taste"]))/(rating_obj.orders+1)
        rating_obj.speed = ((rating_obj.speed * rating_obj.orders) + Decimal(data["speed"]))/(rating_obj.orders+1)
        rating_obj.service = ((rating_obj.service * rating_obj.orders) + Decimal(data["service"]))/(rating_obj.orders+1)
        rating_obj.orders += 1
        rating_obj.save()

        return Response({"order_status": "order received"},status=status.HTTP_200_OK)

average_rating_update_view = AverageRatingUpdateView.as_view()
    


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((TokenAuthentication, SessionAuthentication))
def current_user(request):
    user = request.user
    return Response({
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name
    })







 