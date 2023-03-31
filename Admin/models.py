from django.db import models

# Create your models here.
class Grades(models.Model):
    grades=models.CharField(max_length=100)
    isactive=models.BooleanField(default=False)

    class Meta:
        db_table='Grades'
