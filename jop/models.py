from distutils.command.upload import upload
from unicodedata import category, name
from django.db import models


JOP_TYPE = (
   ('Full Time', 'Full Time'),
   ('Part Time', 'Part Time'),
)
# Create your models here.

def image_upload(instance, fileName):
   imageName, extension = fileName.split(".")
   return "jobs/%s.%s"%(instance.id, extension)

class Jop(models.Model):
   title = models.CharField(max_length=100)
   jop_type = models.CharField(max_length=15, choices= JOP_TYPE)
   description = models.TextField(max_length=1000)
   published_at = models.DateTimeField(auto_now=True)
   vacancy = models.IntegerField(default=1)
   salary = models.IntegerField(default=0)
   experienc = models.IntegerField(default=1)
   category = models.ForeignKey('Category', on_delete=models.CASCADE)
   image = models.ImageField(upload_to=image_upload)
   def __str__(self):
      return self.title




class Category(models.Model):
    name = models.CharField(max_length=55)


    def __str__(self):
       return  self.name       