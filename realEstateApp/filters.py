import django_filters
from django_filters import CharFilter
from .models import *

class SalesFilter(django_filters.FilterSet):
    address = CharFilter(field_name = "address", lookup_expr = "icontains")
    class Meta:
        model = Homesforsale
        fields = '__all__'