from django.db import models

# Create your models here.
class Media(models.Model):
    type_choices = [
        ("Movie", "Movie"),
        ("TV Show", "TV Show")
    ]

    type = models.CharField(max_length=20, choices=type_choices)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    cast = models.TextField()
    country = models.CharField(max_length=255)
    date_added = models.DateField()
    release_year = models.IntegerField()
    rating = models.CharField(max_length=10)
    duration = models.CharField(max_length=15)
    listed_in = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title