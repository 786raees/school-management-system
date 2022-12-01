from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Section,Classes
from .forms import SectionForm,ClassForm
from .table import SectionTable,ClassTable

def create_section(request):
    requested_user_school = request.user.selectedschool.school if request.user.user_type == 'super admin' else request.user.school
    object_list = Section.objects.filter(school=requested_user_school)
    form = SectionForm()
    if request.method == 'POST':
        form = SectionForm(request.POST)
    
        if form.is_valid():
            obj = form.save(commit=False)
            obj.school = requested_user_school
            obj.save()
            form = SectionForm()
            messages.success(request, f'"{obj.school}" Section has been added successfully')
        else:
            messages.warning(request, 'Section has been added unsuccessfully')
        
    context = {
        'object_list': SectionTable(object_list),
        'form': form,
        'page_name': 'Sections',
        'app_name': 'Academics',
    }

    return render(request, 'pages/academics/sections.html', context)

def update_section(request, pk):
    requested_user_school = request.user.selectedschool.school if request.user.user_type == 'super admin' else request.user.school
    object_list = Section.objects.filter(school=requested_user_school)
    _object = Section.objects.get(id=pk, school=requested_user_school)
    form = SectionForm(instance=_object)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=_object)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.school = requested_user_school
            obj.save()
            messages.success(request, f'"{obj.school}" Section has been updated successfully')
            return redirect('academics:create_section')
        else:
            messages.warning(request, 'Section has been updated unsuccessfully')
            
    context = {
        'object_list': SectionTable(object_list),
        'form': form,
        'page_name': 'Sections',
        'app_name': 'Academics',
    }

    return render(request, 'pages/academics/sections.html', context)

def delete_section(request, pk):
    requested_user_school = request.user.selectedschool.school if request.user.user_type == 'super admin' else request.user.school
    try:
        _object = Section.objects.get(id=pk, school=requested_user_school)
        _object.delete()
        messages.success(request, f'"{_object.school}" Section has been deleted successfully')
    except Section.DoesNotExist:
        messages.warning(request, 'Section has been deleted unsuccessfully')
    
    return redirect('academics:create_section')


# CRUD for Classes


def create_class(request):
    requested_user_school = request.user.selectedschool.school if request.user.user_type == 'super admin' else request.user.school
    object_list = Classes.objects.filter(school=requested_user_school)
    form = ClassForm()
    if request.method == 'POST':
        form = ClassForm(request.POST)
    
        if form.is_valid():
            obj = form.save(commit=False)
            obj.school = requested_user_school
            obj.save()
            form = ClassForm()
            messages.success(request, f'"{obj.school}" Class has been added successfully')
        else:
            messages.warning(request, 'Class has been added unsuccessfully')
        
    context = {
        'object_list': ClassTable(object_list),
        'form': form,
        'page_name': 'Class',
        'app_name': 'Academics',
    }

    return render(request, 'pages/academics/class.html', context)

def update_class(request, pk):
    requested_user_school = request.user.selectedschool.school if request.user.user_type == 'super admin' else request.user.school
    object_list = Classes.objects.filter(school=requested_user_school)
    _object = Classes.objects.get(id=pk, school=requested_user_school)
    form = ClassForm(instance=_object)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=_object)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.school = requested_user_school
            obj.save()
            messages.success(request, f'"{obj.school}" Class has been updated successfully')
            return redirect('academics:create_class')
        else:
            messages.warning(request, 'Class has been updated unsuccessfully')
            
    context = {
        'object_list': ClassTable(object_list),
        'form': form,
        'page_name': 'Class',
        'app_name': 'Academics',
    }

    return render(request, 'pages/academics/class.html', context)

def delete_class(request, pk):
    requested_user_school = request.user.selectedschool.school if request.user.user_type == 'super admin' else request.user.school
    try:
        _object = Classes.objects.get(id=pk, school=requested_user_school)
        _object.delete()
        messages.success(request, f'"{_object.school}" Class has been deleted successfully')
    except Classes.DoesNotExist:
        messages.warning(request, 'Class has been deleted unsuccessfully')
    
    return redirect('academics:create_class')