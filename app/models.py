from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=20, null=True)
    password=models.CharField(max_length=20, null=True)
    passwordagain=models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name
    

