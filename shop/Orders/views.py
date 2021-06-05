from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from .models import Order
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import OrderSerializer, OrderDetailSerializer
from rest_framework import permissions
from rest_framework import authentication
from Carts.models import Cart
from Includes.models import Include
# Create your views here.

class OrderViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    authentication_classes = [JSONWebTokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return OrderSerializer
        return OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.filter(memberID=self.request.user) #有修改過

    def perform_create(self, serializer):
        total = 0
        discount_total = 0
        order = serializer.save()
        cart_merchandises = Cart.objects.filter(memberID=self.request.user) #有修改過
        for goods in cart_merchandises:
            order_goods = Include
            order_goods.merchandiseID = goods.merchandiseID
            order_goods.Quantity = goods.Quantity
            order_goods.orderID = order
            total += goods.Quantity * goods.merchandiseID.price
            order_goods.save()
            cart_merchandises.delete()
        '''
        code = order.coupon_code
        coupon_type = Coupon.objects.filter(code=code)
        if code == '':
            discount_total = total
        elif coupon_type < 1:
            discount_total *= coupon_type
        elif coupon_type > 1:
            discount_total -= coupon_type
        '''
        return order


