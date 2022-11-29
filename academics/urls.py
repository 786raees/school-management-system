from django.urls import path
from . import views as academics_views

app_name = "academics"

urlpatterns = [
    path("sections/", academics_views.create_section, name="create_section"),
    path("section/<int:pk>/update/", academics_views.update_section, name="update_section"),
    path("section/<int:pk>/delete/", academics_views.delete_section, name="delete_section"),
]
