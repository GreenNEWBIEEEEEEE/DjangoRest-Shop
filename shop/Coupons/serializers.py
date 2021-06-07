from django.db.models import Sum
from rest_framework import serializers
from .models import Coupon
from Carts.models import Cart

class CouponSerializer(serializers.ModelSerializer):
    discount_total = serializers.SerializerMethodField('get_DiscountTotal')

    def get_DiscountTotal(self, obj):
        cartMerchandises = Cart.objects.filter(member=self.context['request'].user)

        # 如果購物車沒東西
        if (not cartMerchandises):
            return 0

        orderTotal = cartMerchandises.aggregate(Sum('total_price'))['total_price__sum']
        discount_total = orderTotal
        code = obj.code
        coupon_type = obj.type
        if code == '':
            discount_total = orderTotal
        elif coupon_type < 1:
            discount_total *= coupon_type
        elif coupon_type > 1:
            discount_total -= coupon_type
        return discount_total

    class Meta:
        model = Coupon
        fields = '__all__'
