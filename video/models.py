from django.db import models
from django.dispatch.dispatcher import receiver

class VideoUnit(models.Model):
    title = models.CharField(max_length=256)

class VideoFile(models.Model):
    file = models.FileField(upload_to='videos', null=False, default='default.mp4')
    videounit = models.OneToOneField(VideoUnit, on_delete=models.CASCADE, primary_key=True)

@receiver(models.signals.pre_delete, sender=VideoUnit)
def auto_delete_videofile(sender, instance, **kwargs):
    if instance.videofile and instance.videofile.file:
        instance.videofile.delete()