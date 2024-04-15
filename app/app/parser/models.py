from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    published_at = models.DateField()

    def __str__(self):
        return self.title
