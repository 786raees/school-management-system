import contextlib
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

import sweetify

from .table import SchoolInfoTable
from .forms import SelectSchoolForm, SchoolInfoForm
from .models import SchoolInfo, SelectedSchool

User = get_user_model()

def default_school_view(request):
    try:
        request.user.selectedschool
    except SelectedSchool.DoesNotExist:
        sweetify.warning(request, 'Please Add A School', text="Please add a school so you can continue!", persistent='I understand')
        messages.warning(request, "Please add a school so you can continue!")

        return redirect("confurations:school_list_view")
    form = SelectSchoolForm(request.POST or None, instance=request.user.selectedschool)
    school_info_form = SchoolInfoForm(instance=request.user.selectedschool.school)
    if form.is_valid():
        form.save()
        return redirect("confurations:default_school_view")
        
    context = {
               'app_name': 'Configurations',
               'page_name': 'Select Default School',
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
               'app_name': 'Configurations',
               'page_name': 'Select Default School',
               'form': form,
               'school_info_form': school_info_form,
               }
    
    return render(request, 'pages/configuration/school_info.html', context)

def school_list_view(request):
    form = SchoolInfoForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        selectedschool, created = SelectedSchool.objects.get_or_create(user=request.user)
        selectedschool.school = obj
        selectedschool.save()
        sweetify.success(request, 'School Added', text=f'"{obj.school_name}" Schhol has been added successfully')
        messages.success(request, f'"{obj.school_name}" Schhol has been added successfully')
        form = SchoolInfoForm()
    object_list = SchoolInfo.objects.all()
    object_list = SchoolInfoTable(object_list)
    template_name: str = 'pages/configuration/school_list.html'
    context = {
        'object_list': object_list,
        'form': form,
        'app_name': 'Configurations',
        'page_name': 'Add | Delete School',
        }
    return render(request, template_name, context)


def delete_school_view(request, id):
    try:
        school = SchoolInfo.objects.get(id=id, user=request.user)
        with contextlib.suppress(Exception):
            if school == request.user.selectedschool.school:
                sweetify.info(request, 'School Is Selected As Your Default School', text="Please Select An Other School From Here", persistent='I understand')
                messages.info(request, "Please Select An Other School From Here")
                return redirect("confurations:default_school_view")

        school.delete()
        sweetify.success(request, 'School Deleted', text=f'"{school.school_name}" and data linked with it has been deleted successfully')
        messages.success(request, f'"{school.school_name}" and data linked with it has been deleted successfully')
    except SchoolInfo.DoesNotExist:
        sweetify.warning(request, 'School Does Not Exist', text="Please mind your own business!", persistent='I understand')
        messages.warning(request, "Please mind your own business!")

    return redirect("confurations:school_list_view")

