from rest_framework import serializers
from .models import Activity, Event


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'color']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['user', 'activity', 'date']