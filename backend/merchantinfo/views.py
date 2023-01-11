from rest_framework import generics
from .models import MerchantInfo
from .serializers import MerchantInfoSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from myproject.permissions import IsMerchant


# Create your views here.

class MerchantInfoCreateAPIView(generics.CreateAPIView):
    queryset = MerchantInfo.objects.all()
    serializer_class = MerchantInfoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsMerchant]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

merchantinfo_create_view = MerchantInfoCreateAPIView.as_view()

class MerchantInfoListAPIView(generics.ListAPIView):
    queryset = MerchantInfo.objects.all()
    serializer_class = MerchantInfoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsMerchant]
  

merchantinfo_list_view = MerchantInfoListAPIView.as_view()

class MerchantListCreateView(generics.ListCreateAPIView):
    queryset = MerchantInfo.objects.all()
    serializer_class = MerchantInfoSerializer
    authentication_classes = ( TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

merchant_list_create_view = MerchantListCreateView.as_view()

class MerchantGetUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MerchantInfo.objects.all()
    lookup_field = 'pk'
    serializer_class = MerchantInfoSerializer
    authentication_classes = ( TokenAuthentication,SessionAuthentication)
    permission_classes = [IsAuthenticated]
    
merchant_get_update_delete = MerchantGetUpdateDeleteView.as_view()    

