from django.db import models

# Create your models here.
class dataTable(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    state = models.CharField(max_length=50)