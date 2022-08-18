from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from rest_framework import viewsets
from .serializers import LinkSerializer
from .models import Link


class ShortenerView(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class Redirector(View):
    def get(self,request, shorten_url,*args,**kwargs):
        shorten_url=settings.HOST_URL+'/'+self.kwargs['shorten_url']
        redirect_link = Link.objects.filter(shorten_url=shorten_url).first().original_url
        return redirect(redirect_link)

