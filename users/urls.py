from django.urls import path
from . import views as auth_views


app_name = "users"
urlpatterns = [
    path("logout/", auth_views.Log_out_user, name="Log_out_user"),
]
