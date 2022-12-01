from django.urls import path
from . import views as academics_views

app_name = "academics"

urlpatterns = [
    path("sections/", academics_views.create_section, name="create_section"),
    path("section/<int:pk>/update/", academics_views.update_section, name="update_section"),
    path("section/<int:pk>/delete/", academics_views.delete_section, name="delete_section"),
    path("class/", academics_views.create_class, name="create_section"),
    path("class/<int:pk>/update/", academics_views.update_class, name="update_class"),
    path("class/<int:pk>/delete/", academics_views.delete_class, name="delete_class"),
]
