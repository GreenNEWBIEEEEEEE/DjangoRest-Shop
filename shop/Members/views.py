from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import Member
from rest_framework import response
from .serializers import MemberDetailSerializer
from .serializers import MemberRegSerializer
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class MemberViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = User
    queryset = User.objects.all()
    serializer_class = MemberRegSerializer
    authentication_classes = [JSONWebTokenAuthentication, authentication.SessionAuthentication]

    def get_object(self):
        return self.request.user


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["username"] = user.username
        print(re_dict)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'update':
            return [permissions.IsAuthenticated()]
        return []

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MemberDetailSerializer
        elif self.action == "create":
            return MemberRegSerializer

        return MemberDetailSerializer

    def perform_create(self, serializer):
        return serializer.save()


