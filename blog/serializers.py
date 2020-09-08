from rest_framework import serializers

from .models import Blogger

class BloggerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogger
        fields = ('id', 'name', 'age', 'profession', 'gmail', 'gender')