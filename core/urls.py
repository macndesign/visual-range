from django.conf.urls import patterns, url
from core.views import TestSelect2FormView, GMapsTemplateView, PhotoImageListView

urlpatterns = patterns('',
    url(r'^form-select2/$', TestSelect2FormView.as_view(), name='form-select2'),
    url(r'^maps/$', GMapsTemplateView.as_view(), name='maps'),
    url(r'^images/$', PhotoImageListView.as_view(), name='images'),
)
