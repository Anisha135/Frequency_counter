from django.db import models

class frequency_model(models.Model):
    website=models.URLField(max_length=200)
    def __str__(self):
        return self.website

class count_model(models.Model):
    count=models.CharField(max_length=100)

