from rest_framework import serializers
from .models import Order
from Includes.serializers import IncludeSerializer
class OrderSerializer(serializers.ModelSerializer):
    OrderGoods = IncludeSerializer
    class Meta:
        model = Order
        fields = ['coupon_code', 'shipping_type', 'payment_type']


class OrderDetailSerializer(serializers.ModelSerializer):
    OrderGoods = IncludeSerializer
    class Meta:
        model = Order
        fields = '__all__'