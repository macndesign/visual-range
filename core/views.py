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
    success_url = '/admin/'

    def form_valid(self, form):

        # Salvar a UF
        uf_descricao = form.cleaned_data['administrative_area_level_1_long_name']
        uf_abreviatura = form.cleaned_data['administrative_area_level_1']
        uf = Uf()

        try:
            uf = Uf.objects.get(abreviatura=uf_abreviatura)
            messages.add_message(self.request, messages.WARNING, u'A UF já existe.')

        except Uf.DoesNotExist:
            uf.abreviatura = uf_abreviatura
            uf.descricao = uf_descricao
            uf.save()
            messages.add_message(self.request, messages.SUCCESS, u'UF cadastrada com sucesso.')

        # Salvar a cidade associada a UF
        cidade_descricao = form.cleaned_data['locality']
        cidade = Cidade()

        try:
            cidade = Cidade.objects.get(descricao=cidade_descricao)
            messages.add_message(self.request, messages.WARNING, u'A cidade já existe.')
        except Cidade.DoesNotExist:
            cidade.descricao = cidade_descricao
            cidade.uf = uf
            cidade.save()
            messages.add_message(self.request, messages.SUCCESS, u'Cidade cadastrada com sucesso.')

        # Salvar o bairro associado a uma cidade
        bairro_descricao = form.cleaned_data['sublocality']
        bairro = Bairro()

        try:
            bairro = Bairro.objects.get(descricao=bairro_descricao)
            messages.add_message(self.request, messages.WARNING, u'O bairro já existe.')
        except Bairro.DoesNotExist:
            bairro.descricao = bairro_descricao
            bairro.cidade = cidade
            bairro.save()
            messages.add_message(self.request, messages.SUCCESS, u'Bairro cadastrado com sucesso.')

        return redirect(reverse('test:maps'))
