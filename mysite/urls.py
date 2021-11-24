from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('admin/', admin.site.urls),

    path('api/test', views.Api.test, name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
