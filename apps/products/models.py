from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class Company(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    index = models.IntegerField(default=0)
    
    
class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(default='')
    producer = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    characteristics = models.TextField(null=True, blank=True)#JSONField()

    
class Review(models.Model):
    subject = models.CharField(max_length=500)
    text = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    

class GalleryImage(models.Model):
    mane = models.CharField(max_length=500)
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
