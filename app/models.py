from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user  = models.ForeignKey(User, on_delete= models.CASCADE,default=1)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField(max_length=11   )
    myid = models.AutoField(primary_key=True)
    
    
    def __str__(self):
        return self.name