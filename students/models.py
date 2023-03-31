from django.db import models
from schools.models import schoolregister
from Admin.models import Grades
# Create your models here.


class student(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    grades=models.ForeignKey(Grades,on_delete=models.CASCADE)
    school=models.ForeignKey(schoolregister,on_delete=models.CASCADE)

    class Meta:
        db_table='student'