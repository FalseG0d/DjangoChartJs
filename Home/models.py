from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Sales(models.Model):
    point_of_contact = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sales = models.FloatField()
    
    def __str__(self):
        return self.point_of_contact