from rest_framework import viewsets
from microbiome_api.models import Entry
from .serializers import EntrySerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
