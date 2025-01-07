from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from .models.models import FoodItem
from .form import FoodItemForm

def home(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food item added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Failed to add food item. Please check the form.')
    else:
        form = FoodItemForm()

    food_items = FoodItem.objects.all().order_by('name')
    total_calories = food_items.aggregate(total=Sum('calories'))['total'] or 0

    return render(request, 'home.html', {
        'food_items': food_items,
        'total_calories': total_calories,
        'form': form,
    })

def delete_food(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    food_item.delete()
    messages.success(request, 'Food item deleted successfully!')
    return redirect('home')

def reset_calories(request):
    FoodItem.objects.all().delete()
    messages.success(request, 'Calorie count reset for the day!')
    return redirect('home')
