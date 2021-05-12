from djongo import models


class Video(models.Model):
    name = models.CharField(max_length=255)
    
    def get_snapshot_uri(self) -> str:
        return 'https://www.gizbot.com/images/2020-09/realme-7_159921061900.jpg'
