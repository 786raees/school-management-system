from django.shortcuts import render, redirect
from .forms import SelectSchoolForm, SchoolInfoForm
# Create your views here.
def home(request):
    form = SelectSchoolForm(request.POST or None, instance=request.user.selectedschool)
    school_info_form = SchoolInfoForm(request.POST or None, instance=request.user.selectedschool.school)
    if form.is_valid():
        form.save()
        return redirect("confurations:config_views")
        
    context = {
               'form': form,
               'school_info_form': school_info_form,
               }
    return render(request, 'pages/configuration/school_info.html', context)