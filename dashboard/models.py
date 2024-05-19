from django.db import models

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=100)
    embed_code = models.TextField()
    
    def __str__(self):
        return self.title