from django.db import models

# Create your models here.
class Book(models.Model):

    name = models.CharField(max_length=10)
    desc=models.TextField(max_length=250)
    
    def __str__(self):
        return self.name;    
        
        

