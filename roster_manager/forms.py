from django import forms
from .models import Player, Position

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'
