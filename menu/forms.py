from django import forms
from .models import *


class MealSetupForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = '__all__'


class DishSetupForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'



class MealWiseDishForm(forms.ModelForm):
    class Meta:
        model = MealwiseDish
        fields = '__all__'