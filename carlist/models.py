from django.db import models

# Create your models here.
class Car(models.Model):
	# The car brand : Innova/Land Cruiser/Fortuner SMALL FIX AMOUNT COULD USE AS DICTIONARY
    car_brand = models.CharField(max_length=20)
    car_subbrand = models.CharField(max_length=20)
    car_product_year = models.CharField(max_length = 4)
    car_bought_year = models.CharField(max_length=4)
    car_color = model.CharField(max_length = 15)
    
# Car journal book
class CarJournal(models.Model):
	journal_date = models.DateField()
