from django.db import models

class Snapshot(models.Model):
    file = models.ImageField(upload_to='snapshots', default='default.jpg')

class VideoFile(models.Model):
    file = models.FileField(upload_to='videos', default='default.mp4')

def get_default_videofile():
    return VideoFile.objects.create(file='default.mp4')

class Video(models.Model):
    name = models.CharField(max_length=255)
    snapshot = models.OneToOneField(Snapshot, on_delete=models.CASCADE, null=True)
    videofile = models.OneToOneField(VideoFile, on_delete=models.CASCADE, null=False, default=get_default_videofile)

    def __str__(self):
        return self.name
