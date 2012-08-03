from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from blog_rest.forms import FormRestAjax

admin.autodiscover()

# api
from tastypie.api import Api
from blog_rest.api import EntryResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^report/', include('django_xhtml2pdf.urls', namespace='report')),
    url(r'^test/', include('core.urls', namespace='test')),
    # url(r'^visual_range/', include('visual_range.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Api
    # (r'^api/', include(v1_api.urls)),
    # url(
    #     r'^send-ajax/',
    #     FormView.as_view(
    #         template_name='blog_rest/form_ajax_send.html',
    #         form_class=FormRestAjax,
    #         success_url='/send-ajax/',
    #     ),
    #     name='send-ajax'
    # ),

    # Basic usage of django Tasty Pie
    (r'^api/', include('basic.api.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
