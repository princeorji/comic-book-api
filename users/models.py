from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Artist(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    biography = models.CharField(max_length=225)
    is_currently_employed = models.BooleanField()

    def __str__(self):
        return self.user_id.get_username()

class Series(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.name

class Issue(models.Model):
    name = models.CharField(max_length=255)
    issue_number = models.CharField(max_length=25)
    publication_date = models.DateField()
    artist_id = models.ForeignKey('Artist', on_delete=models.CASCADE)
    series_id = models.ForeignKey('Series', on_delete=models.CASCADE)

    def __str__(self):
        return self.name