from django.urls import path
from . import views as config_views

app_name = "confurations"

urlpatterns = [
    path("", config_views.home, name="config_views")
]
