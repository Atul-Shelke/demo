from django.db import models

# Create your models here.
class schoolregister(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.BigIntegerField()
    password=models.CharField(max_length=100)
    access=models.TextField(default='acs')
    refresh=models.TextField(default='ref')

    class Meta:
        db_table='schoolregister'