from django.urls import path
from . import views as config_views

app_name = "confurations"

urlpatterns = [
    path("", config_views.default_school_view, name="default_school_view"),
    path("schools/", config_views.add_delete_school_view, name="add_delete_school_view"),
    path("update_school_info/", config_views.update_school_info, name="update_school_info")
]
