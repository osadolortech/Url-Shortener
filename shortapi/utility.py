from random import choices
from string import ascii_letters
from django.conf import settings


def shortener(model_instance):
    model_class = model_instance.__class__
    while True:
        random_string = ''.join(choices(ascii_letters,k=6))
        new_link = settings.HOST_URL+'/'+random_string
        if not model_class.objects.filter(shorten_url=new_link).exists():
            break
    return new_link

