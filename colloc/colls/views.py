from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from django.core.urlresolvers import reverse
from .forms import CorpForm, SettingsForm
from .models import corpus
from colloc.settings import MEDIA_ROOT
import os
import nltk
import string
import math



def read_corp(corp):
    corpus = open(os.path.join(MEDIA_ROOT + corp))
    return corpus


def tokenize(corpus):
    text = nltk.tokenize(corpus)
    return text


def calc_mean(dif_list):  # calculates mean of difference
    suum = sum(dif_list)
    mean = suum / len(dif_list)
    return mean


def std_dev(dif_list, mean):  # calculates standard of deviation of differences
    square_list = [(x - mean) ** 2 for x in dif_list]
    suum = sum(square_list)
    dev = math.sqrt(suum / (len(square_list) - 1))
    return dev


def values(text, word, wind, min_count):
    texts = text.lower()
    co_tot_dic = {}
    indices_dif = {}
    stop = list(string.punctuation)
    full_stop = ['–','`', '\'']
    stop.extend(full_stop)
    tokens = nltk.word_tokenize(texts)
    indices = ([i for i, j in enumerate(tokens) if j == word])  # finds indices of word in texts
    for i in indices:
        frame = tokens[(i - wind):(i + wind)]  # finds window of word based on given window value
        new_i = 0 + wind  # index of main word within frame.
        for w in frame:
            ind = frame.index(w)
            dif = ind - new_i  # index dif
            if w in co_tot_dic.keys():  # finds and counts all possible collocates in every context
                co_tot_dic[w][0] += 1
                indices_dif[w].append(dif)  # will append all distance differences to a word
            else:
                co_tot_dic[w] = [1]
                indices_dif[w] = [dif]
    for k, v in list(co_tot_dic.items()):  # removes entries seen only three times and stop word/punctuation.
        if v[0] < min_count or k in stop or k == word:  # maybe we can make this an option as well
            del co_tot_dic[k]
    for k in list(co_tot_dic.keys()):  # finds total counts for possible collocates
        co_tot_dic[k].append(len([c for c in tokens if c == str(k)]))  # append to dictionary list for word "k"
        k_mean = calc_mean(indices_dif[k])
        co_tot_dic[k].append(k_mean)  # append mean of coll k
        co_tot_dic[k].append(std_dev(indices_dif[k], k_mean))  # append std of dev of coll k
    token_tot = len(tokens)
    word_tot = len(indices)
    return (token_tot, word_tot, co_tot_dic)


def chi_sq(vals):
    chi_dic = {}
    w1 = vals[1]  # key word in corpus without collocates
    none = vals[0] - w1  # all tokens in corpus without key word and collocate
    for token, val in vals[2].items():
        w2 = val[1] - val[0]  # amount of every colocate in corpus
        both = val[0]  # amount of every collocation in corpus
        chi_dic[token] = (vals[0]) * (both * none - w1 * w2) ** 2 / (both + w2) * (both + w1) * (both + none) * (none + w1)
    return chi_dic


def loglike(vals):
    log_dic = {}
    n1 = vals[1]
    n = vals[0]
    for token, val in vals[2].items():
        k1 = val[0]
        x1 = k1 / n1
        k2 = val[1] - k1
        n2 = n - n1
        x2 = k2 / n2
        p = val[1] / n
        try:
            one = math.log((p ** k1) * (1 - p) ** (n1 - k1))
        except ValueError:
            one = 0
        try:
            two = math.log((p ** k2) * (1 - p) ** (n2 - k2))
        except ValueError:
            two = 0
        try:
            three = math.log((x1 ** k1) * (1 - x1) ** (n1 - k1))
        except ValueError:
            three = 0
        try:
            four = math.log((x2 ** k2) * (1 - x2) ** (n2 - k2))
        except ValueError:
            four = 0
        log_dic[token] = (-2) * (one + two - three - four)
    return log_dic


def mutual(vals):
    d = {}
    ws = vals[0]
    px = vals[1]
    nmbrs = vals[2]
    for token in nmbrs:
        val = nmbrs[token]
        pxy = val[0]
        py = val[1]
        pmi = math.log((pxy * ws) / (px * py), 2)
        d[token] = pmi
    return d


def organize(vals, chi, pmi, logs):
    final = {}
    for coll, val in vals[2].items():
        final.update({coll: [val[0], val[2], val[3], chi[coll], pmi[coll], logs[coll]]})
    return final


def home(request):
    form = SettingsForm()
    return render(request, 'colls/home.html', {
        'form': form
    })


def results(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid:
            form.save()
            with open(os.path.join(MEDIA_ROOT, form.cleaned_data['corp']), 'r', encoding='utf-8') as file:
                corp = file.read()
            min_count = form.cleaned_data['min_count']
            word = form.cleaned_data['word']
            window = form.cleaned_data['window']
            vals = values(corp, word, window, min_count)
            chi = chi_sq(vals)
            logs = loglike(vals)
            pmi = mutual(vals)
            final = organize(vals, chi, pmi, logs)
            return render(request, 'colls/results.html', {
                'final': final,
            })
    else:
        return render(request, 'colls/results.html')


def upload(request):
    if request.method == 'POST':
        form = CorpForm(request.POST, request.FILES)
        if form.is_valid():
            doc = corpus(corp = request.FILES['corp'])
            doc.user = request.user
            form.save()
            return redirect(reverse('home'))
    else:
        form = CorpForm()
    return render(request, 'colls/upload.html', {
        'form': form
    })







