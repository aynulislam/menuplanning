from django.urls import path
from menu import views


urlpatterns = [

    path('', views.menuDashboard,name='menuDashboard' ),
    
    path('mealSetup', views.mealSetup, name='meal_setup'),
    path('addMealSetup', views.addMealSetup, name='add_meal_setup'),
    path('viewMealSetup', views.viewMealSetup, name='view_meal_setup'),
    path('updateMealSetup', views.updateMealSetup, name='update_meal_setup'),
    path('deleteMealSetup/<id>/', views.deleteMealSetup, name='delete_meal_setup'),


    path('dishSetup', views.dishSetup, name='dish_setup'),
    path('addDishSetup', views.addDishSetup, name='add_dish_setup'),
    path('viewDishSetup', views.viewDishSetup, name='view_dish_setup'),
    path('updateDishSetup', views.updateDishSetup, name='update_dish_setup'),
    path('deleteDishSetup/<id>/', views.deleteDishSetup, name='delete_dish_setup'),



    path('mealDishDashboard', views.mealDishDashboard, name='meal_dish_dashboard'),
    path('addDishWiseMeal', views.addDishWiseMeal, name='add_dish_wise_meal'),
]
