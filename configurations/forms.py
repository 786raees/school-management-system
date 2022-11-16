from django import forms
from django_select2 import forms as s2forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Row, Submit, Button, Column

from .models import SelectedSchool, SchoolInfo

    
class SchoolInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(Field('management_name'), css_class='col-md-6',),
                Div(Field('school_name'), css_class='col-md-6',),
                css_class='row',
            ),
            Div(
                Div(Field('school_short_name'), css_class='col-md-6',),
                Div(Field('school_code'), css_class='col-md-6',),
                css_class='row',
            ),
            Div(
                Div(Field('address'), css_class='col-md-6',),
                Div(Field('phone'), css_class='col-md-6',),
                css_class='row',
            ),
            Div(
                Div(Field('session'),),
            ),
        )
        super().__init__(*args, **kwargs)
    
    
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