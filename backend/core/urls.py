from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/common/", include("common.urls")),
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
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
