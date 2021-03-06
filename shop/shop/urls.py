"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from Merchandises.views import MerchandisesViewSet
from Orders.views import OrderViewSet
from Members.views import MemberViewSet
from django.urls import include
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from Carts.views import CartViewSet
from Coupons.views import CouponViewSet

router = DefaultRouter()

router.register(r'merchandise', MerchandisesViewSet, basename="merchandises")
router.register(r'member', MemberViewSet, basename="member")
router.register(r'order', OrderViewSet, basename="order")
router.register(r'cart', CartViewSet, basename="cart")
router.register(r'coupon', CouponViewSet, basename="coupon")
#router.register(r'merchandise', MerchandisesViewSet, basename="merchandises")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('jwt-auth/', obtain_jwt_token),
]
