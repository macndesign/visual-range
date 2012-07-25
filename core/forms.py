# coding=utf-8
from django import forms

class TestForm(forms.Form):
    test = forms.ChoiceField(widget=forms.Select(attrs={'style': 'width: 300px'}))
