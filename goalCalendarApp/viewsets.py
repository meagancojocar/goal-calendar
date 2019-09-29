from rest_framework import viewsets
from .models import Activity, Event
from .serializers import ActivitySerializer, EventSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer