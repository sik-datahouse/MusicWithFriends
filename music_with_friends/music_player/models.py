from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)

class Position(models.Model):
    # time when the video was played the last time
    time = models.TimeField(auto_now=True, auto_now_add=False)
    # seconds in the video when it was played
    time_in_video = models.models.IntegerField()

class QueueEntry(models.Model):
    video_url = models.URLField(max_length=200)

class Room(models.Model):
    name = models.CharField(max_length=20)
    users = models.ArrayModelField(model_container=QueueEntry)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    queue = models.ArrayModelField(model_container=QueueEntry)