from django.db import models

# Create your models here.
class Word(models.Model):
   name = models.CharField(max_length=100)
   name_ar = models.CharField(max_length=100)
   create_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.name

