from video import views as video_views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', video_views.catalog),
    path('watch/', video_views.watch_video),
    path('upload/', video_views.upload_video),
    path('delete/', video_views.delete_video),
    path('tags/', video_views.get_tags),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
