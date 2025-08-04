from django.db import models

class AlbumModel(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"
