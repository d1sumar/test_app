from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from monitoring.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),

] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', index_view, name="home"),
    path('test/', include('monitoring.urls')),
    path('user/', include('user.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)