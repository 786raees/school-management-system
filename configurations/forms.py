from django import forms
from django_select2 import forms as s2forms

from .models import SelectedSchool, SchoolInfo

    
class SchoolInfoForm(forms.ModelForm):
    class Meta:
        model = SchoolInfo
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'session': s2forms.Select2Widget(attrs={'class': 'form-control select2'})
        }
    
class SelectSchoolForm(forms.ModelForm):
    class Meta:
        model = SelectedSchool
        
        fields = ('school',)
        widgets = {
            'school': s2forms.Select2Widget(attrs={'class': 'form-control select2'})
        }