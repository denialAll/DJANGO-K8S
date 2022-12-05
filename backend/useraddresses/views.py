from django.shortcuts import render
from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication

# Create your views here.


class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

address_list_create_view = AddressListCreateView.as_view()

class AddressGetUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    lookup_field = 'pk'
    serializer_class = AddressSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]

address_get_update_delete = AddressGetUpdateDeleteView.as_view()    