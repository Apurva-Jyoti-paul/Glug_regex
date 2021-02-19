from django.db import models


class Texts(models.Model):
    maintext=models.TextField(max_length=2000,default='lorem ipsum')
    searchtext=models.TextField(max_length=60,default='d')


# Create your models here.
