from django.db import models
from django.contrib.auth.models import User
from colloc.settings import MEDIA_ROOT
import os


def corp_list(path):
    for root,dirs,files in os.walk(path):
        return files

class corpus(models.Model):
    user = models.ForeignKey(User, default = 1)
    corp = models.FileField(upload_to=MEDIA_ROOT)


class query(models.Model):
    user = models.ForeignKey(User, default = 1)
    if not corp_list(MEDIA_ROOT):
        corp_choices = (('None', 'None'),)
    else:
        corp_choices = tuple((str(x), str(x)) for x in corp_list(MEDIA_ROOT))
    corp = models.FileField(
        choices = corp_choices,
        default = 'None' ,
    )
    window_choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    window = models.IntegerField(
        choices = window_choices,
        default = 1
    )
    min_choices = ((2, '2'), (3, '3'), (4, '4'), (5, '5'))
    min_count = models.IntegerField(
        choices = min_choices,
        default = 1
    )
    word = models.CharField(max_length=50)
