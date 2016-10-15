from django import forms
from .models import corpus, query

class CorpForm(forms.ModelForm):
    class Meta:
        model = corpus
        fields = ('corp',)

class SettingsForm(forms.ModelForm):
    class Meta:
        model = query
<<<<<<< HEAD
        fields = ('corp', 'window', 'rang', 'word',)
=======
        fields = ('corp', 'window', 'rang', 'word')
>>>>>>> 5fde28adc1994e430be04d8d96d05522c2dfa4fd
