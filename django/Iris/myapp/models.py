from django.db import models

# Create your models here.


class IrisDb(models.Model):
    sepal_length=models.CharField(max_length=100,null=True,blank=True)
    sepal_width=models.CharField(max_length=200,null=True,blank=True)
    petal_length=models.CharField(max_length=100,null=True,blank=True)
    petal_width=models.CharField(max_length=100,null=True,blank=True)
