from django.db import models

class Films(models.Model):
    film_id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    release_year = models.IntegerField()

    