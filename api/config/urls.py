"""Main URLs module."""

from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    path('', include(('apps.users.urls', 'users'), namespace='users')),
    path('', include(('apps.hits.urls', 'hits'), namespace='hits')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
