from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone_number=models.CharField(max_length=200,null=True)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name