from rest_framework import serializers
from .models import Member
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
User = get_user_model()

class MemberDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['nickname','phone','address','email','activated']

class MemberRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','nickname','phone','address','email']
        username = serializers.CharField(required=True, allow_blank=False,validators=[UniqueValidator(queryset=User.objects.all(), message="帳號已存在")])


    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user