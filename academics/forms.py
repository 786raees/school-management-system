from django import forms
from .models import Section,Classes

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('name',)

class ClassForm(forms.ModelForm):
    """Model Form to handle class"""
    class Meta:
        model = Classes
        fields = ('classes','section')

        widgets = {
            'section': forms.CheckboxSelectMultiple()
        }
