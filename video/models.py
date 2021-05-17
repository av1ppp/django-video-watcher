from django.db import models
from django.dispatch.dispatcher import receiver
import shutil
from os import path
from django.conf import settings

class VideoUnit(models.Model):
    """ Видео как целый объект """
    title = models.CharField(max_length=255)

    def get_root_dir(self):
        return str(self.id)

        
def videofile_path(instance, filename):
    return f'{instance.videounit.get_root_dir()}/{filename}'

@receiver(models.signals.pre_delete, sender=VideoUnit)
def auto_delete_videounit(sender, instance, **kwargs):
    if instance.videofile and instance.videofile.file:
        instance.videofile.file.delete()
    if instance.videothumbnail and instance.videothumbnail.file:
        instance.videothumbnail.file.delete()

    shutil.rmtree(path.join(settings.MEDIA_ROOT, instance.get_root_dir()))

class VideoFile(models.Model):
    """ Видео как файл """
    file = models.FileField(upload_to=videofile_path, null=False)
    videounit = models.OneToOneField(VideoUnit, on_delete=models.CASCADE,
        primary_key=True)
    
    def __str__(self):
        return self.file.name

def videothumbnail_path(instance, filename):
    return f'{instance.videounit.get_root_dir()}/{filename}'

class VideoThumbnail(models.Model):
    """ Миниатюра для видео """
    file = models.ImageField(upload_to=videothumbnail_path, null=True)
    videounit = models.OneToOneField(VideoUnit, on_delete=models.CASCADE,
        primary_key=True)

