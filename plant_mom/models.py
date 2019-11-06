from django.db import models

# Create your models here.


class Plant(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    care_tips = models.TextField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name
