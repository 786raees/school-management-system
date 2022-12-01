from django import forms
from .models import Section,Classes

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('name',)
class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ('classes','section')