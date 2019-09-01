from django.db import models

#Here we will define our models, Like customer, employee etc. It will the be exported my django
#into postgres server

class DVD(models.Model):
    
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    inStock = models.BooleanField(default=False)