from django import forms
from .models import Section,Classes

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('name',)

class ClassForm(forms.ModelForm):
    """Model Form to handle class"""
    section = forms.ModelMultipleChoiceField(
        queryset=Section.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True)
    class Meta:
        model = Classes
        fields = ('classes','section')

    def __init__(self, *args, **kwargs):
        self.school = kwargs.pop("school")
        super(ClassForm, self).__init__(*args, **kwargs)
        self.fields["section"].queryset = self.school.section_set.all()
