from django.contrib import admin
from .models import SchoolInfo, SelectedSchool

@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    '''Admin View for SchoolInfo'''

    list_display = ("user","school_name","phone","email")
    list_filter = ("user",)
    search_fields = ("user","school_name")


@admin.register(SelectedSchool)
class SelectedSchoolAdmin(admin.ModelAdmin):
    '''Admin View for SelectedSchool'''

    list_display = ("user","school")
    list_filter = ("user","school")
    search_fields = ("user","school")