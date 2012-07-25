# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from core.forms import TestForm

class TestSelect2FormView(FormView):
    template_name = 'core/test_form.html'
    form_class = TestForm

class TestMapsTemplateView(TemplateView):
    template_name = 'core/test_maps.html'
