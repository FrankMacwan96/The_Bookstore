from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'MyAppIADS/', include('MyAppIADS.urls')),
    path(r'', include('django.contrib.auth.urls')),
    url(r'^$', TemplateView.as_view(template_name='MyApp/index.html'),
        name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)