from api.models import api_model
from rest_framework import serializers


class api_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=api_model
        fields='__all__'