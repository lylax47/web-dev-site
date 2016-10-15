from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from django.core.urlresolvers import reverse
from .forms import CorpForm, SettingsForm



def home(request):
<<<<<<< HEAD
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse('results'))
    else:
        form = SettingsForm()
    return render(request, 'colls/home.html', {
        'form': form
    })
=======
    return render(request, 'colls/home.html')
>>>>>>> 5fde28adc1994e430be04d8d96d05522c2dfa4fd



def upload(request):
    if request.method == 'POST':
        form = CorpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = CorpForm()
    return render(request, 'colls/upload.html', {
        'form': form
    })

<<<<<<< HEAD

=======
def settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse('results'))
    else:
        form = SettingsForm()
>>>>>>> 5fde28adc1994e430be04d8d96d05522c2dfa4fd


