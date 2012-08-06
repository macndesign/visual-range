from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from basic.forms import NoteForm

class BasicFormView(FormView):
    template_name='test_form.html'
    form_class=NoteForm
    success_url='/basic-form/'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(BasicFormView, self).dispatch(request, *args, **kwargs)


class BasicAjaxFormView(TemplateView):
    template_name='test.html'
    success_url='/basic/'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(BasicAjaxFormView, self).dispatch(request, *args, **kwargs)
