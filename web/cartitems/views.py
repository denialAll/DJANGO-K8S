from rest_framework import generics
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication
from django.db.models import Q
from django_k8s.paginations import StandardResultsSetPagination

# Create your views here.


class CartItemListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
    
cart_item_list_create_view = CartItemListCreateView.as_view()

class CartItemGetUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    lookup_field = 'pk'
    serializer_class = CartItemSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
    
cart_item_get_update_delete = CartItemGetUpdateDeleteView.as_view()    

class NewCartItemListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = CartItem.objects.all().filter(product__merchant = self.request.user).filter(cart__is_accepted = None)
        return qs
    
new_cart_item_list = NewCartItemListView.as_view()

class AcceptedCartItemListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = CartItem.objects.all().filter(product__merchant = self.request.user).filter(cart__is_accepted = True)
        return qs

accepted_cart_item_list = AcceptedCartItemListView.as_view()

class NewAcceptedCartItemListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = CartItem.objects.all().filter(product__merchant = self.request.user).filter(~Q(cart__is_accepted  = False))
        return qs

new_accepted_cart_item_list = NewAcceptedCartItemListView.as_view()

class CustomerPreviousOrdersListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        qs = CartItem.objects.all().filter(cart__customer  = self.request.user).order_by('-id')
        return qs

customer_previous_orders_list = CustomerPreviousOrdersListView.as_view()

class MerchantPreviousOrdersListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        qs = CartItem.objects.all().filter(product__merchant  = self.request.user).filter(cart__is_sent = True).order_by('-id')
        return qs

merchant_previous_orders_list = MerchantPreviousOrdersListView.as_view()