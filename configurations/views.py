from django.shortcuts import render, redirect
from django.contrib import messages
from .table import SchoolInfoTable
from .forms import SelectSchoolForm, SchoolInfoForm
from .models import SchoolInfo


def default_school_view(request):
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
    object_list = SchoolInfo.objects.all()
    object_list = SchoolInfoTable(object_list)
    template_name: str = 'pages/configuration/school_list.html'
    context = {
        'object_list': object_list,
        'app_name': 'Configurations',
        'page_name': 'Add | Delete School',
        }
    return render(request, template_name, context)

def delete_school_view(request, id):
    school = SchoolInfo.objects.get(id=id)
    # TODO: uncomment if done
    # school.delete()
    messages.success(request, f'"{school.school_name}" and data linked with it has been deleted successfully')
    return redirect("confurations:school_list_view")
