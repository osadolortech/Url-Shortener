from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ShortenerView

router=DefaultRouter()
router.register('shortener',ShortenerView)

urlpatterns = [
    path("",include(router.urls))
]