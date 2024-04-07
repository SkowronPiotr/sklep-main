from django import forms 
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category' : forms.Select(attrs={
                'style': ''
            }),
            'name' : forms.TextInput(attrs={
                'style': 'width: 300px; background-color: white; color: #666; border: 2px solid #ddd; border-radius: 15px; font-size: 20px; padding: 10px;',
            }),
            'description' : forms.Textarea(attrs={
                'style': 'width: 100%; height: 200px; border-radius: 15px;'
            }),
            'price' : forms.TextInput(attrs={
                'style': 'width: 300px; background-color: white; color: #666; border: 2px solid #ddd; border-radius: 15px; font-size: 20px; padding: 10px;',
            }),
            'image' : forms.FileInput(attrs={
                'style': ''
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold',)
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': ''
            }),
            'description' : forms.Textarea(attrs={
                'class': ''
            }),
            'price' : forms.TextInput(attrs={
                'class': ''
            }),
            'image' : forms.FileInput(attrs={
                'class': ''
            }),
        }