from django.db import models

# Create your models here.

class jsp(models.Model):
    Name=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)
    mail=models.EmailField()
    phno=models.IntegerField()

    def __str__(self):
        return self.Name