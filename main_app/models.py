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
   date = models.DateField("Maintenance Date", default=datetime.date.today)
   technician = models.CharField(max_length=50,  null=True, blank=True)
   description = models.TextField()
   piano = models.ForeignKey(Piano, on_delete=models.CASCADE)

   def __str__(self):
        return f'{self.date}  - {self.technician}'

class Performer(models.Model):

    STLYE_CHOICES = [
        ('classical', 'Classical'),
        ('jazz', 'Jazz'),
        ('rock and roll', 'Rock and Roll'),
        ('pop', 'Pop'),
        ('ragtime', 'Ragtime'),
        ('boogie-Woogie', 'Boogie-Woogie'),
        ('contemporary', 'Contemporary'),
    ]

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    years_of_experience = models.IntegerField()
    style = models.CharField(max_length=15, choices=STLYE_CHOICES)

    def __str__(self):
        return f'{self.name} - Style: {self.style}'
