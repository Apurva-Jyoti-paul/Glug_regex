from django.db import models


class Texts(models.Model):
    maintext=models.TextField(max_length=2000,default='lorem ipsum')
    searchtext=models.TextField(max_length=60,default='d')

class ocr(models.Model):
    name=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='pdfs/')
# Create your models here.
