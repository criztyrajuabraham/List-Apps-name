from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(max_length=800)
    year=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name