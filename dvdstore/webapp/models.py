from django.db import models

# Create your models here.

class DVD(models.Model):
    
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    inStock = models.BooleanField(default=False)