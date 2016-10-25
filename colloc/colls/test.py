from colloc.settings import MEDIA_ROOT

def corp_list():
    for root,dirs,files in os.walk('{0}user_{1}'.format(MEDIA_ROOT, user_id)):
        return files