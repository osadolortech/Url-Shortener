from django.conf import settings
from django.db import models
from user.models import User
from random import choices
from string import ascii_letters



class Link(models.Model):
    user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    original_url = models.URLField()
    shorten_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def shortener(self):
        while True:
            random_string = ''.join(choices(ascii_letters,k=6))
            new_link = settings.HOST_URL+'/'+random_string
            if not Link.objects.filter(shorten_url=new_link).exists():
                break
        return new_link

    def save(self,*args,**kwargs):
        if not self.shorten_url:
            new_link = self.shortener()
            self.shorten_url=new_link
        return super().save(*args,**kwargs)

