from django.db import models

# Create your models here.

class DVD:
    id : int
    name : str
    img : str
    desc : str
    price : int
    inStock : bool