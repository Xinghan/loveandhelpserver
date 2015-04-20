from django import forms
from news.models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        # exclude = ['author', 'updated', 'created', ]
