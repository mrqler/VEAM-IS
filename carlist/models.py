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
    proposed_date = models.DateField()
    journal_date = models.DateField()
    odo_start = models.IntegerField(max_length=6)
    odo_end = models.IntegerField(max_length=6)
    #Devision that proposing the care
    proposing_devision = models.CharField(max_length=20)
    #head of devision that propose the car who approve the car request
    proposing_approver = models.CharField(max_length=20)
    #asigned driver

    #Staff who assign this order to driver

    #Head of Administrative devision who approve this order and assignment

    #destination 1, destination 2 ...

    #Expensediture

    
