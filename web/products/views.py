from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication
from django_k8s.permissions import IsMerchant
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
# Create your views here.

logger = logging.getLogger(__name__)

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(merchant=self.request.user)

product_create_view = ProductCreateAPIView.as_view()

class AllProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all().filter()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
  

all_product_list_view = AllProductListAPIView.as_view()


class MerchantProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user)
        qs = Product.objects.all().filter(merchant = self.request.user)
        return qs
        
merchant_product_list_view = MerchantProductListAPIView.as_view()

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,SessionAuthentication)

    def get_queryset(self):
        print(self.request.user)
        qs = Product.objects.all().filter(merchant = self.request.user)
        return qs

product_rud_view = ProductRetrieveUpdateDestroyAPIView.as_view()

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

product_detail_view = ProductRetrieveAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [IsMerchant]

product_destroy_view = ProductDestroyAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

product_update_view = ProductUpdateAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        qs = Product.objects.all().filter(merchant = self.request.GET["restaurantId"]).filter(is_available = true)
        return qs 
    

product_list_view = ProductListAPIView.as_view()
