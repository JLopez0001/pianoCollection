from django.db import models
import datetime  

# Create your models here.
class Piano(models.Model):

    TYPE_CHOICES = [
        ('grand', 'Grand'),
        ('upright', 'Upright'),
        ('digital', 'Digital'),
        ('electronic', 'Electronic'),
    ]

    brand = models.CharField(max_length=100)
    weight = models.IntegerField()
    number_of_keys = models.IntegerField()
    type = models.CharField(max_length=11, choices=TYPE_CHOICES)
    condition = models.CharField(max_length=50)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.brand

class MaintenanceRecord(models.Model):
   date = models.DateField("Maintenance Date", default=datetime.date.today),
   technician = models.CharField(max_length=50),
   description = models.TextField()
   piano = models.ForeignKey(Piano, on_delete=models.CASCADE)
   print(piano)
   def __str__(self):
        return f'{self.date}  - {self.technician}'

