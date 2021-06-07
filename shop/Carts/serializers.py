from rest_framework import serializers
from .models import Cart
from Merchandises.serializers import MerchandiseSerializer
'''
class CartDetailSerializer(serializers.ModelSerializer):
    merchandise = MerchandiseSerializer(many=False, read_only=True)
    class Meta:
        model = Cart
        fields = ["merchandise", "Quantity", "total_price"]
'''
class CartDetailSerializer(serializers.ModelSerializer):
    merchandise = MerchandiseSerializer(many=False, read_only=True)
    #Total = serializers.SerializerMethodField('get_Total')

    def get_Total(self, obj):
        return obj.Quantity * obj.merchandise.price
    class Meta:
        model = Cart
        fields = ["merchandise", "Quantity", "total_price"]
        #fields = ["merchandise", "Quantity", "total_price", 'Total']


class CartSerializer(serializers.ModelSerializer):

    # 有了這個，添加到購物車的時候，不用輸入會員名字。
    #member = serializers.HiddenField(
    #    default=serializers.CurrentUserDefault()
    #)

    class Meta:
        model = Cart
        fields = ["merchandise", "Quantity"]
        extra_kwargs = {'merchandise': {'read_only': False}}