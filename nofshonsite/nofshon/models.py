from django.db import models

# Create your models here.

class Disease(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

class Child(models.Model):
    child_name = models.CharField(max_length=200)
    age = models.DecimalField(decimal_places=2, max_digits=5)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def __str__(self):
        return self.child_name


