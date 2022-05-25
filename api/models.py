from django.db import models

# Create your models here.


class AddProduct(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField(max_length=2000,null=True,blank=True)
    price=models.IntegerField(default=0)
    def __str__(self) :
        return self.title



