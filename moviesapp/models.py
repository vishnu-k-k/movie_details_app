from django.db import models

# Create your models here.
class movies(models.Model):
        name=models.CharField(max_length=250)
        year=models.IntegerField()
        descr=models.TextField()
        img=models.ImageField(upload_to='movie_pics')

        def __str__(self):
         return self.name