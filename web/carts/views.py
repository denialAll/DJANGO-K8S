from rest_framework import generics
from rest_framework.views import APIView
from .models import Cart
from .serializers import CartSerializer
from cartitems.models import CartItem  
from cartitems.serializers import CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class CartCustomView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        cart = request.data["cart"]
        cart_serializer = CartSerializer(data=cart)
        if cart_serializer.is_valid():
            cart_serializer.validated_data.update({"customer":request.user})
            cart_object = Cart.objects.create(**cart_serializer.validated_data)
           
            items = request.data["cartList"]

            for item in items:
                item_serializer = CartItemSerializer(data=item)
                if item_serializer.is_valid():
                    item_serializer.validated_data.update({"cart":cart_object})
                    cart_item = CartItem.objects.create(**item_serializer.validated_data) 
            
            
            return Response({"order_status": "order received"},status=status.HTTP_200_OK)
        return Response({"order_status": "validation failed"},status=status.HTTP_400_BAD_REQUEST)

cart_custom_view = CartCustomView.as_view()



class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer = self.request.user)

cart_list_create_view = CartListCreateView.as_view()

class CartGetUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    lookup_field = 'pk'
    serializer_class = CartSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]

cart_get_update_delete = CartGetUpdateDeleteView.as_view()    


class CartListNewOrders(generics.ListAPIView):
    serializer_class = CartSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Cart.objects.all().filter(merchant = self.request.user).filter(is_accepted = None)
        return qs

cart_list_new_orders = CartListNewOrders.as_view()

class CartListAcceptedOrders(generics.ListAPIView):
    serializer_class = CartSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Cart.objects.all().filter(merchant = self.request.user).filter(is_accepted = True)
        return qs

cart_list_accepted_orders = CartListAcceptedOrders.as_view()
    

