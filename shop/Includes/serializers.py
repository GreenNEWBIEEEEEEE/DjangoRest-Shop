from rest_framework import serializers
from .models import Include
from Merchandises.serializers import MerchandiseSerializer
class IncludeSerializer(serializers.ModelSerializer):
    merchandises = MerchandiseSerializer(many=False)
    class Meta:
        model = Include
        fields = '__all__'
