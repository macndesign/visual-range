from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'django_xhtml2pdf.views.index', name='index'),
    url(r'^download/$', 'django_xhtml2pdf.views.download', name='download'),
    url(r'^ezpdf-sample/$', 'django_xhtml2pdf.views.ezpdf_sample', name='ezpdf-sample'),
)
