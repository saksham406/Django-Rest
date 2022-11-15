from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

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

class Review(models.Model):
    ratings = models.PositiveIntegerField(validators=[ MinValueValidator(1),MaxValueValidator(5) ])
    description = models.CharField(null=True, max_length=300)
    watchlist = models.ForeignKey(WatchList, on_delete= models.CASCADE, related_name = 'reviews')
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now= True)

    def __str__(self):
        return self.description +' ratings '+str(self.ratings)