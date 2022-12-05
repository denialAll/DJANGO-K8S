from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication
from myproject.permissions import IsMerchant
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

# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         print(request.headers)
#         return Response(serializer.data)

# product_list_view = SnippetList.as_view()


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
    permission_classes = [IsMerchant]

product_update_view = ProductUpdateAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        print("This is the GET params", self.request.GET)
        qs = Product.objects.all().filter(merchant = self.request.GET["restaurantId"])
        return qs 
    

product_list_view = ProductListAPIView.as_view()
