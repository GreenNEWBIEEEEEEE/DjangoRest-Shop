from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import CouponSerializer
from .models import Coupon
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import permissions
from rest_framework import authentication
# Create your views here.
class CouponViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = CouponSerializer
    authentication_classes = [JSONWebTokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Coupon.objects.filter(member=self.request.user, available=True)
