from django import forms
from .models import corpus, query

class CorpForm(forms.ModelForm):
    class Meta:
        model = corpus
        fields = ('corp',)

class SettingsForm(forms.ModelForm):
    class Meta:
        model = query
        fields = ('corp', 'window', 'word', 'min_count',)