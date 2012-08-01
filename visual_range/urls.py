from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django_xhtml2pdf.views import ReportTemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^report/$', ReportTemplateView.as_view(), name='report'),
    url(r'^download/$', 'django_xhtml2pdf.views.download', name='download'),
    url(r'^sample/$', 'django_xhtml2pdf.views.ezpdf_sample', name='sample'),

    url(r'^test/', include('core.urls', namespace='test')),
    # url(r'^visual_range/', include('visual_range.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
