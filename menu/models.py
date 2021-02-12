from django.db import models

# Create your models here.


class Meal(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    modified_by = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    modified =  models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    modified_by = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class MealwiseDish(models.Model):
    meal_date = models.DateField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    craeted_by = models.IntegerField()
    modified_by = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)





