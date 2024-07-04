from django.db import models

# Create your models here.
class student(models.Model):
    # migraid = models.AutoField()
    name=models.CharField(max_length=100)
    age=models.ImageField()
    email=models.EmailField()
    address=models.TextField(null=True,blank=True)
    image=models.ImageField()
    file=models.FileField()

class Product(models.Model):
    pass
class Car(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)
 

