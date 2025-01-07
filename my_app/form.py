from django import forms
from .models.models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Food Name'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Calories'}),
        }