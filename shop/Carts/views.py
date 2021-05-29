from django.shortcuts import render
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets,mixins
from .serializers import CartSerializer
from .serializers import CartDetailSerializer
from rest_framework import permissions
from rest_framework import authentication
from .models import Cart
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