import django_filters

from common.filters import BaseModelFilter
from notes.models import Notes


class NotesFilter(BaseModelFilter):
    class Meta:
        model = Notes
        fields = {
            'title': ['exact', 'icontains'],
            'status': ['exact'],
            'user': ['exact'],
            # 'created_at': ['exact', 'year__gt', 'year__lt'],
        }
