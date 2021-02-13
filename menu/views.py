from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.




def menuDashboard(request):
    return render (request, 'menuDashboard.html')

    

def mealSetup(request):
    all_meal = Meal.objects.all().order_by('-pk')
    context = {
        'all_meal' : all_meal

    }
    return render(request, 'meal.html', context)



def addMealSetup(request):
    try:
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['name'] = request.POST.get('name').lower()
            request.POST['created_by'] = 1
            request.POST['modified_by'] = 1
            request.POST['status'] = True
            form = MealSetupForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                if Meal.objects.filter(name=name).exists():
                    message = 'Meal already exists'
                    messages.warning(request, message)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    form.save()
                    message = 'Meal added successfully'
                    messages.success(request, message)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                message = 'Form is not valid....check form again!'
                messages.warning(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            message = "Check Method Please....Method Invalid"
            messages.warning(request,message)
            return HttpResponseRedirect(request>META.get('HTTP_REFERER'))
    except:

        message = "Try again... Meal can not be add now"
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@csrf_exempt
def viewMealSetup(request):
    getMealSetupById = Meal.objects.filter(id=request.POST.get('id')).values()
    return JsonResponse({'getMealSetupById': list(getMealSetupById)})



def updateMealSetup(request):
    getMealSetupById = Meal.objects.get(id = request.POST.get('id'))
    request.POST = request.POST.copy()
    request.POST['name'] = request.POST.get('name').lower()
    request.POST['status'] = True
    request.POST['created_by'] = 1
    request.POST['modified_by'] = 1

    try:
        form = MealSetupForm(instance=getMealSetupById)
        if request.method == 'POST':
            form = MealSetupForm(request.POST, instance=getMealSetupById)
            if form.is_valid():
                if Meal.objects.filter(name = request.POST['name']).exists():
                    messsage = 'this meal already exists'
                    messages.warning(request, message)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    form.save()
                    message = 'meal info updated successfully!'
                    messages.success(request, message)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                message = 'form is not valid...check form again!'
                messages.success(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            message = 'method is not valid....check method!'
            messages.warning(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        message = 'try again...! update cannot perform right now!'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
 

 

def deleteMealSetup(request,id):
    try:
        getMealSetupById = Meal.objects.get(id=id)
        if getMealSetupById.status == True:
            getMealSetupById.status = False
            getMealSetupById.save()
            message = 'Meal status change sucsessfully'
            messages.success(request,message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif getMealSetupById.status == False:
            getMealSetupById.status = True
            getMealSetupById.save()
            message = 'Meal status change sucsessfully'
            messages.success(request,message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            message = 'Problem changing status for meal'
            messages.warnig(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        message = 'Try again....! Meal status can not channging....'
        messages.warning(request,message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def dishSetup(request):
    all_dish = Dish.objects.all().order_by('-pk')
    print(all_dish)
    context = {
        'all_dish' : all_dish

    }
    print(context)
    return render(request, 'dish.html', context)


    

def addDishSetup(request):
    try:
        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['name'] = request.POST.get('name').lower()
            request.POST['created_by'] = 1
            request.POST['modified_by'] = 1
            request.POST['status'] = True
            form = DishSetupForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                print(name)
                if Dish.objects.filter(name=name).exists():
                    message = 'Dish already exists'
                    messages.warning(request, message)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    form.save()
                    message = 'Dish added successfully'
                    messages.success(request, message)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                message = 'Form is not valid'
                messages.warning(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            message = "Check Method Please....Method Invalid"
            messages.warning(request,message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        message = "Try again... Dish can not be add now"
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@csrf_exempt
def viewDishSetup(request):
    getDishSetupById = Dish.objects.filter(id=request.POST.get('id')).values()
    return JsonResponse({'getDishSetupById': list(getDishSetupById)})


def updateDishSetup(request):
    getDishSetupById = Dish.objects.get(id = request.POST.get('id'))
    request.POST = request.POST.copy()
    request.POST['name'] = request.POST.get('name').lower()
    request.POST['status'] = True
    request.POST['created_by'] = 1
    request.POST['modified_by'] = 1

    try:
        form = DishSetupForm(instance=getDishSetupById)
        if request.method == 'POST':
            form = DishSetupForm(request.POST, instance=getDishSetupById)
            if form.is_valid():
                if Dish.objects.filter(name = request.POST['name']).exists():
                    messsage = 'this dish already exists'
                    messages.warning(request, message)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    form.save()
                    message = 'dish info updated successfully!'
                    messages.success(request, message)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                message = 'form is not valid...check form again!'
                messages.success(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            message = 'method is not valid....check method!'
            messages.warning(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        message = 'try again...! update cannot perform right now!'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
 

 

def deleteDishSetup(request,id):
    try:
        getDishSetupById = Dish.objects.get(id=id)
        if getDishSetupById.status == True:
            getDishSetupById.status = False
            getDishSetupById.save()
            message = 'Dish status change sucsessfully'
            messages.success(request,message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif getDishSetupById.status == False:
            getDishSetupById.status = True
            getDishSetupById.save()
            message = 'Dish status change sucsessfully'
            messages.success(request,message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            message = 'Problem changing status for meal'
            messages.warnig(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        message = 'Try again....! Dish status can not channging....'
        messages.warning(request,message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


from .models import Meal, Dish

def mealDishDashboard(request):
    all_meal = Meal.objects.all()
    all_dish = Dish.objects.all()
    all_meal_wise_dish = MealwiseDish.objects.all()
    context = {
        'all_meal':all_meal, 
        'all_dish': all_dish,
        'all_meal_wise_dish' : all_meal_wise_dish
    }
    return render(request, 'mealDishDashboard.html',context)





def addDishWiseMeal(request):
    if request.method == 'POST':
        getDate = request.POST.get('meal_date')
        getMeal = request.POST.getlist('meal')
        getDish = request.POST.getlist('dish')
        print('fucking loop',len(getMeal))
        for i in range(0,len(getMeal)):
            data = {
               'meal_date': getDate,
               'meal': getMeal[i],
               'dish':  getDish[i],
               'craeted_by': 1,
               'modified_by': 1 
            }
            print(data)
            mealWiseDish = MealWiseDishForm(data)
            if mealWiseDish.is_valid():
                mealWiseDish.save()
                
            else:
                for field in mealWiseDish:
                    for error in field.errors:
                        messages.warning(request, "%s : %s" % (field.name, error))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        message = 'done'
        messages.success(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    else:
        print('not a post method')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))













