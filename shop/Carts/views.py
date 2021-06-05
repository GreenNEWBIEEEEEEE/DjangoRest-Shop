from django.shortcuts import render
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets,mixins
from .serializers import CartSerializer
from .serializers import CartDetailSerializer
from rest_framework import permissions
from rest_framework import authentication
from .models import Cart
from .models import Merchandise
#from custom.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
# Create your views here.

class CartViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin , mixins.CreateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = CartSerializer
    authentication_classes = [JSONWebTokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'merchandise' #用在Retrieve上面的

    def get_serializer_class(self):
        if self.action == 'list':
            return CartDetailSerializer
        else:
            return CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(member=self.request.user)


    # 如果serializer沒有hidden field的話，override此方法，這樣也可以不用傳送memberID進行添加
    def perform_create(self, serializer):
        try:
            exitstedMerchandise = Cart.objects.get(member=self.request.user, merchandise=serializer.validated_data['merchandise'])
        except Cart.DoesNotExist:
            exitstedMerchandise = None

        # 以下是避免用戶購買重複東西，造成duplicate
        # 如果資料庫已有相同的key，就直接update資料庫
        if (exitstedMerchandise != None):
            #existedMerchandise適從資料庫拿出來的object，因此必須用.{屬性}access，
            #serializer的data是dict，所以要用[]，除此之外，serializer如果要access Data，只能使用validated_data
            exitstedMerchandise.Quantity += serializer.validated_data['Quantity']
            exitstedMerchandise.save()
        else:
            serializer.save(member=self.request.user)


'''
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        merchandises = self.get_queryset()
        total = 0
        for sum in merchandises:
            total += sum
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
'''