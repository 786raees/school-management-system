from django.shortcuts import render, redirect
from .forms import SelectSchoolForm, SchoolInfoForm
# Create your views here.

def default_school_view(request):
    form = SelectSchoolForm(request.POST or None, instance=request.user.selectedschool)
    school_info_form = SchoolInfoForm(instance=request.user.selectedschool.school)
    if form.is_valid():
        form.save()
        return redirect("confurations:default_school_view")
        
    context = {
               'app_name': 'configurations',
               'page_name': 'select_default_school',
               'form': form,
               'school_info_form': school_info_form,
               }
    return render(request, 'pages/configuration/school_info.html', context)

def update_school_info(request):

    form = SelectSchoolForm(instance=request.user.selectedschool)
    school_info_form = SchoolInfoForm(request.POST or None, instance=request.user.selectedschool.school)

    if school_info_form.is_valid():
        school_info_form.save()
        return redirect("confurations:default_school_view")

    context = {
               'app_name': 'configurations',
               'page_name': 'select_default_school',
               'form': form,
               'school_info_form': school_info_form,
               }
    
    return render(request, 'pages/configuration/school_info.html', context)

