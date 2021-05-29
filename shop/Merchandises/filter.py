import django_filters
from .models import Merchandise

class MerchandisesFilter(django_filters.rest_framework.FilterSet):
    price_less = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_greater = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    class Meta:
        model = Merchandise
        fields = ['price_less', 'price_greater']