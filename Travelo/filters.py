import django_filters
from .models import Travel

class OrderFilter(django_filters.FilterSet) :
    class Meta:
        model = Travel
        fields = '__all__'