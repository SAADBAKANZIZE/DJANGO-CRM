from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
class Product(models.Model):


    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    tag=models.ManyToManyField(Tag)


    def __str__(self):
        return self.name