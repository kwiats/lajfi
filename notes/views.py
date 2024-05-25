from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from notes.models import Notes
from notes.serializers import NotesSerializer
from notes.filters import NotesFilter

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NotesFilter
