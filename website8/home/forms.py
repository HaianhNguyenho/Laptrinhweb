from django import forms
from .models import svModel
class svform(forms.ModelForm):
    class Meta:
        model = svModel
        fields = ['name', 'mssv', 'birth_day', 'lop', 'image' ]