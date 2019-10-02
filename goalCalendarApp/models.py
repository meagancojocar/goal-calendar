from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Activity(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_activity', default=0)

    def __str__(self):
        return self.name


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_event', default=0)
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE, related_name='activity_events', default=0)
    date = models.DateField(verbose_name='date')