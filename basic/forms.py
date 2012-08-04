from django import forms
from basic.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
