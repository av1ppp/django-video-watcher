from django.db import models
from django.dispatch.dispatcher import receiver
from django.conf import settings
import uuid
import os
import shutil

class VideoUnit(models.Model):
    """ Видео как целый объект """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)

    def get_root_dir(self) -> str:
        return settings.MEDIA_ROOT + '/' + str(self.id)

        
def videofile_path(instance, filename):
    return f'{instance.videounit.get_root_dir()}/{filename}'

@receiver(models.signals.pre_delete, sender=VideoUnit)
def auto_delete_videounit(sender, instance, **kwargs):
    shutil.rmtree(instance.get_root_dir())

class VideoFile(models.Model):
    """ Видео как файл """
    file = models.FileField(upload_to=videofile_path, null=False)
    videounit = models.OneToOneField(VideoUnit, on_delete=models.CASCADE,
        primary_key=True)
    
    def __str__(self) -> str:
        return self.file.name

def videothumbnail_path(instance, filename):
    return f'{instance.videounit.get_root_dir()}/{filename}'

class VideoThumbnail(models.Model):
    """ Миниатюра для видео """
    file = models.ImageField(upload_to=videothumbnail_path, null=True)
    videounit = models.OneToOneField(VideoUnit, on_delete=models.CASCADE,
        primary_key=True)

