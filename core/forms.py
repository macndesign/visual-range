# coding=utf-8
from django import forms

# Test Select2
class TestForm(forms.Form):
    test = forms.ChoiceField(widget=forms.Select(attrs={'style': 'width: 300px'}))

# Test Form Maps
class GMapsForm(forms.Form):
    sublocality = forms.CharField(
        label='Bairro',
        help_text='Propriedade "sublocality" da API do Google Maps.',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
    )
    locality = forms.CharField(
        label='Cidade',
        help_text='Propriedade "locality" da API do Google Maps.',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
    )
    administrative_area_level_1 = forms.CharField(
        label='UF',
        help_text='Propriedade "administrative_area_level_1" da API do Google Maps.',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
    )

    administrative_area_level_1_long_name = forms.CharField(
        label=u'UF Descrição',
        help_text='Propriedade "administrative_area_level_1" da API do Google Maps.',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
    )
