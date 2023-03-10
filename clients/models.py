from django.db import models

# Create your models here.


class Clients(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')
    description = models.TextField()
    location = models.CharField(max_length=100)


class Meta:
    verbose_name_plural = 'clients'

    def __str__(self):
        return self.name
