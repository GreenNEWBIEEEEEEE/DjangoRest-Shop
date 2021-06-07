from django.db.models import Sum
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
from .models import Coupon


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
        cartMerchandises = Cart.objects.filter(member=self.request.user)
        orderTotal = cartMerchandises.aggregate(Sum('total_price'))['total_price__sum']
        code = serializer.validated_data['coupon_code']
        my_coupon = Coupon.objects.get(code=code)
        coupon_type = my_coupon.type
        discount_total = orderTotal
        if code == '':
            discount_total = orderTotal
        elif coupon_type < 1:
            discount_total *= coupon_type
        elif coupon_type > 1:
            discount_total -= coupon_type

        # 不能coupon delete，不然Include會出錯
        #my_coupon.delete()
        my_coupon.available = False
        my_coupon.save()
        cartMerchandises.delete()

        serializer.save(memberID=self.request.user, total_price=orderTotal, discount_price=discount_total)

