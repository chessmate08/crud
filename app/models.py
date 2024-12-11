from django.db import models

# Create your models here.
class student(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.BigIntegerField()

    def __str__(self) :
        return f'{self.FirstName}'