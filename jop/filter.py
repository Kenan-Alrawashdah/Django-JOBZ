from dataclasses import fields
import django_filters
from .models import Jop


class JopFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Jop
        fields = '__all__'
        exclude = ['user', 'price', 'image', 'vacancy', 'salary', 'experienc', 'published_at']
