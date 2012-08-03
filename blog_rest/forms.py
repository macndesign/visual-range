from django import forms
from blog_rest.models import Entry

class FormRestAjax(forms.ModelForm):
    class Meta:
        model = Entry
