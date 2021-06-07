from django.db.models import Sum
from django.shortcuts import render
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets,mixins
from .serializers import CartSerializer
from .serializers import CartDetailSerializer
from rest_framework import permissions
from rest_framework import authentication
from .models import Cart
from .models import Merchandise
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
        try:
            exitstedMerchandise = Cart.objects.get(member=self.request.user, merchandise=serializer.validated_data['merchandise'])
        except Cart.DoesNotExist:
            exitstedMerchandise = None

        # 以下是避免用戶購買重複東西，造成duplicate
        # 如果資料庫已有相同的key，就直接update資料庫
        if (exitstedMerchandise != None):
            #existedMerchandise適從資料庫拿出來的object，因此必須用.{屬性}access，
            #serializer的data是dict，所以要用[]，除此之外，serializer如果要access Data，只能使用validated_data
            exitstedMerchandise.Quantity += serializer.validated_data['Quantity']
            exitstedMerchandise.total_price = exitstedMerchandise.merchandise.price * exitstedMerchandise.Quantity
            exitstedMerchandise.save()
        else:
            # serializer.validated_data是OrderedDict
            # 這邊serializer.validated_data['merchandise']拿出來的是一個object，要注意，雖然前端傳送id
            # 但是serializer的data已經處理過了，已經可以直接拿object
            print(serializer.validated_data)
            print(serializer.validated_data['merchandise'])
            print(serializer.validated_data['merchandise'].id)
            print()
            t = Merchandise.objects.get(pk=serializer.validated_data['merchandise'].id)
            serializer.save(member=self.request.user, total_price=t.price * serializer.validated_data['Quantity'])
    def list(self, request, *args, **kwargs):
        resp = super().list(request, args, kwargs)
        #{'total_price__sum': 13800}
        print(type(resp.data))
        # resp.data是個list，裡面有很多dict，[ OrderedDict, OrderedDict]
        #print(self.get_queryset().aggregate(Sum('total_price')))
        resp.data.append({'sum': self.get_queryset().aggregate(Sum('total_price'))['total_price__sum']})
        return resp