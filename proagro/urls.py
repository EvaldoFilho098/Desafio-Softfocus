from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_set import OcurredEventViewSet, ProductorViewSet, TillageViewSet


router = DefaultRouter()
router.register(r"productor", ProductorViewSet)
router.register(r"ocurredevent", OcurredEventViewSet)
router.register(r"tillage", TillageViewSet)


urlpatterns = [
    path("", include(router.urls))
]