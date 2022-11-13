from django.db import models

# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=40) 
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=200) 

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform , on_delete=models.CASCADE , related_name = "watchlist" )
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title