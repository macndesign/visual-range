from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^report/', include('django_xhtml2pdf.urls', namespace='report')),
    url(r'^test/', include('core.urls', namespace='test')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Basic usage of django Tasty Pie
    (r'^api/', include('basic.api.urls', namespace='api')),
    url(r'^basic/', TemplateView.as_view(template_name='test.html'), name='basic'),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
