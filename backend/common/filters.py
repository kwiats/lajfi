import django_filters

from common.models import BaseModel


class BaseModelFilter(django_filters.FilterSet):
    is_deleted = django_filters.BooleanFilter()
    created_at = django_filters.DateFromToRangeFilter()
    updated_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = BaseModel
        fields = ['created_at', 'updated_at', "is_deleted"]
