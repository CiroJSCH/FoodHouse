from django import forms
from .models import Recipe


class CreateRecipeForm(forms.ModelForm):
    banner = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'hidden', 'accept': 'image/*', 'id': 'file-input'}),
    )

    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full focus:outline-none border-2 border-primary p-2 drop-shadow-md font-text',
            'placeholder': 'e.g: Burgers with fries',
            'id': 'title',
        })
    )

    body = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'w-full focus:outline-none border-2 border-primary p-2 drop-shadow-md font-text resize-none',
            'id': 'body',
            'rows': 5,
        })
    )

    duration = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'w-full focus:outline-none border-2 border-primary p-2 drop-shadow-md font-text',
            'id': 'duration',
        })
    )

    difficulty = forms.ChoiceField(
        required=True,
        choices=Recipe.DIFFICULTY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full focus:outline-none border-2 border-primary p-2 drop-shadow-md font-text h-[43px]',
            'id': 'difficulty',
        })
    )

    categories = forms.MultipleChoiceField(
        required=True,
        choices=Recipe.CATEGORY_CHOICES,
        widget=forms.CheckboxSelectMultiple()
    )

    # Un json field
    ingredients = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'h-0 w-0 p-0 border-0',
        })
    )

    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['author', 'likes_count', 'created_at', 'updated_at']
