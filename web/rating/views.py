from rest_framework import generics
from .models import Rating
from rest_framework.views import APIView
from .serializers import RatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status


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

class RatingsForUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Rating.objects.all()
        print(qs)
    
        return Response({"order_status": "order received"},status=status.HTTP_200_OK)

ratings_for_user = RatingsForUser.as_view()

#  authentication_classes = [TokenAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     parser_classes = [JSONParser]

#     def post(self, request):
#         cart = request.data["cart"]
#         cart_serializer = CartSerializer(data=cart)
#         if cart_serializer.is_valid():
#             cart_serializer.validated_data.update({"customer":request.user})
#             cart_object = Cart.objects.create(**cart_serializer.validated_data)
           
#             items = request.data["cartList"]

#             for item in items:
#                 item_serializer = CartItemSerializer(data=item)
#                 if item_serializer.is_valid():
#                     item_serializer.validated_data.update({"cart":cart_object})
#                     cart_item = CartItem.objects.create(**item_serializer.validated_data) 
            
            
#             return Response({"order_status": "order received"},status=status.HTTP_200_OK)
#         return Response({"order_status": "validation failed"},status=status.HTTP_400_BAD_REQUEST)

# cart_custom_view = CartCustomView.as_view()
