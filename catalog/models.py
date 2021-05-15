from django.db import models
from django.dispatch.dispatcher import receiver

class VideoFile(models.Model):
    file = models.FileField(upload_to='videos', default='default.mp4')

@receiver(models.signals.pre_delete, sender=VideoFile)
def auto_delete_videofile(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()

def get_default_videofile():
    return VideoFile.objects.create(file='default.mp4')

class Video(models.Model):
    name = models.CharField(max_length=255)
    videofile = models.OneToOneField(VideoFile, on_delete=models.CASCADE, null=False, default=get_default_videofile)

    def __str__(self):
        return self.name

@receiver(models.signals.pre_delete, sender=Video)
def auto_delete_video(sender, instance, **kwargs):
    if instance.videofile and instance.videofile.file:
        instance.videofile.file.delete()