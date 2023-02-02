from rest_framework import serializers
from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'number', 'seats', 'busy')


class TableBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'seats', 'busy', 'visitor_name', 'start_time', 'message')
        read_only_fields = ['seats', 'busy']
