from django.db import models

class VideoCodec(models.Model):
    name = models.CharField(max_length=255)

class AudioCodec(models.Model):
    name = models.CharField(max_length=255)