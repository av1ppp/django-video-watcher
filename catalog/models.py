from django.db import models

class Snapshot(models.Model):
    image = models.ImageField(upload_to='snapshot', default='default.jpg')

class Video(models.Model):
    name = models.CharField(max_length=255)
    snapshot = models.OneToOneField(Snapshot, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
