from rest_framework.routers import DefaultRouter
from .views import NginxLogViewSet
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'parse_logs', NginxLogViewSet)

urlpatterns = router.urls
