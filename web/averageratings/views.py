from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import AverageRating
from .serializers import AverageRatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class AverageRatingListCreateView(generics.ListCreateAPIView):
    queryset = AverageRating.objects.all()
    serializer_class = AverageRatingSerializer
    authentication_classes = ( TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

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
        rating_obj.taste = ((rating_obj.taste * rating_obj.orders) + data["taste"])/(rating_obj.orders+1)
        rating_obj.speed = ((rating_obj.speed * rating_obj.orders) + data["speed"])/(rating_obj.orders+1)
        rating_obj.service = ((rating_obj.service * rating_obj.orders) + data["service"])/(rating_obj.orders+1)
        rating_obj.orders += 1
        rating_obj.save()

        return Response({"order_status": "order received"},status=status.HTTP_200_OK)

average_rating_update_view = AverageRatingUpdateView.as_view()
    




    # cart = request.data["cart"]
    #     cart_serializer = CartSerializer(data=cart)
    #     if cart_serializer.is_valid():
    #         cart_serializer.validated_data.update({"customer":request.user})
    #         cart_object = Cart.objects.create(**cart_serializer.validated_data)
           
    #         items = request.data["cartList"]

    #         for item in items:
    #             item_serializer = CartItemSerializer(data=item)
    #             if item_serializer.is_valid():
    #                 item_serializer.validated_data.update({"cart":cart_object})
    #                 cart_item = CartItem.objects.create(**item_serializer.validated_data) 
            
            
    #         return Response({"order_status": "order received"},status=status.HTTP_200_OK)
    #     return Response({"order_status": "validation failed"},status=status.HTTP_400_BAD_REQUEST)





 