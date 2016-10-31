from django.db import models


class BufferArea(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.IntegerField()
    info = models.TextField()


class DangerousArea(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.IntegerField()
    info = models.TextField()


class Location(models.Model):
    user = models.ForeignKey("User")
    time = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Message(models.Model):
    sender = models.ForeignKey("User", related_name="send_user")
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


