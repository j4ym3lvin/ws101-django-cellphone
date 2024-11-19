from django import forms
from .models import Cellphone

class CellphoneForm(forms.ModelForm):
    class Meta:
        model = Cellphone
        fields = ['brand', 'model', 'release_date', 'price']