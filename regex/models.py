from django.db import models


class Texts(models.Model):
    maintext=models.TextField(max_length=500,default='lorem ipsum')
    searchtext=models.TextField(max_length=20,default='d')


# Create your models here.
