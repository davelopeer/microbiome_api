from rest_framework import serializers
from microbiome_api.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'access_id', 'kingdom', 'specie', 'sequence')
