from rest_framework import serializers
from news.models import Entry

class EntrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Entry
        resource_name = 'entry'
        fields = ('id', 'author', 'title', 'body', 'created', 'photo', 'slug')
        lookup_field = 'slug'
