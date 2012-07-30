# coding=utf-8
# Create your views here.
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from core.forms import TestForm, GMapsForm
from core.models import Uf, Cidade, Bairro

class TestSelect2FormView(FormView):
    template_name = 'core/test_form.html'
    form_class = TestForm

class GMapsTemplateView(FormView):
    template_name = 'core/test_maps.html'
    form_class = GMapsForm

    def get_success_url(self):
        return redirect(reverse('test:maps'))

    def form_valid(self, form):
        # Salvar a UF
        uf_descricao = form.cleaned_data['administrative_area_level_1_long_name']
        uf_abreviatura = form.cleaned_data['administrative_area_level_1']
        uf, uf_created = Uf.objects.get_or_create(abreviatura=uf_abreviatura, descricao=uf_descricao)

        if uf_created:
            messages.add_message(self.request, messages.SUCCESS, u'Estado cadastrado com sucesso.')
        else:
            messages.add_message(self.request, messages.WARNING, u'O estado informado já foi cadastrado.')

        # Salvar a cidade associada a UF
        cidade_descricao = form.cleaned_data['locality']
        cidade, cidade_created = Cidade.objects.get_or_create(descricao=cidade_descricao, uf=uf)

        if cidade_created:
            messages.add_message(self.request, messages.SUCCESS, u'Cidade cadastrada com sucesso.')
        else:
            messages.add_message(self.request, messages.WARNING, u'A cidade informada já foi cadastrada.')

        # Salvar o bairro associado a uma cidade
        bairro_descricao = form.cleaned_data['sublocality']
        bairro, bairro_created = Bairro.objects.get_or_create(descricao=bairro_descricao, cidade=cidade)

        if bairro_created:
            messages.add_message(self.request, messages.SUCCESS, u'Bairro cadastrado com sucesso.')
        else:
            messages.add_message(self.request, messages.WARNING, u'O bairro informado já foi cadastrado.')

        return redirect(reverse('test:maps'))
