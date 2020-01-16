from rest_framework import routers
from .api import LeadViewSet
from .views import TestView
from django.conf.urls import url

router = routers.DefaultRouter()
router.register('api/amb_app', LeadViewSet, 'amb_app')
urlpatterns = router.urls

 