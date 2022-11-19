from django.urls import path
from . import views as config_views

app_name = "confurations"

urlpatterns = [
    path("", config_views.default_school_view, name="default_school_view"),
    path("schools/", config_views.school_list_view, name="school_list_view"),
    path("school/<int:id>/delete", config_views.delete_school_view, name="delete_school_view"),
    path("update_school_info/", config_views.update_school_info, name="update_school_info")
]
