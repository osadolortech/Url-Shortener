from django.db import models
from user.models import User
from django.db.models.signals import pre_save
from .utility import shortener





class Link(models.Model):
    user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    original_url = models.URLField()
    shorten_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self,*args,**kwargs):
        if not self.shorten_url:
            self.shorten_url = shortener(self)
        return super().save(*args,**kwargs)

def link_pre_save(instance,*args,**kwargs):
    if not instance.shorten_url:
        new_link = instance.shortener
        instance.shorten_url=new_link
pre_save.connect(link_pre_save,sender=Link)


