"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include

urlpatterns = [
    path("api/", include("common.urls")),
    path("api/notes/", include("notes.urls")),
    path("api/location/", include("location.urls")),
    path("api/motivation/", include("motivation.urls")),
    path("api/progress/", include("progress.urls")),
    path("api/reminder/", include("reminder.urls")),
    path("api/schedule/", include("schedule.urls")),
    path("api/shopping/", include("shopping.urls")),
    path("api/task/", include("task.urls")),
    path("admin/", admin.site.urls),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
