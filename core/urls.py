from django.conf.urls import patterns, url
from core.views import TestSelect2FormView, TestMapsTemplateView

urlpatterns = patterns('',
    url(r'^form-select2/$', TestSelect2FormView.as_view(), name='form-select2'),
    url(r'^maps/$', TestMapsTemplateView.as_view(), name='maps'),
)
