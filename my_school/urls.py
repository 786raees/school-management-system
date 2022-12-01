from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("select2/", include("django_select2.urls")),
    path('configurations/', include('configurations.urls')),
    path('academics/', include('academics.urls')),
    # path('__debug__/', include('debug_toolbar.urls')),

]

# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
