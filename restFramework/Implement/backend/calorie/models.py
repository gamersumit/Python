from django.db import models

# Create your models here.
class CalorieChart(models.Model):
    item_name = models.CharField(max_length=120, null= False, blank = False)
    description = models.CharField(max_length=100000, null= True, blank = True)
    is_cal_per_kg = models.BooleanField(default = False)
    is_cal_per_item = models.BooleanField(default = False)
    is_cal_per_liter = models.BooleanField(default = False)
    calories = models.DecimalField(max_digits = 7, decimal_places = 2, null = False, blank = False)

