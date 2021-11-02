from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import User_locationViewSet

router = DefaultRouter()
router.register("user_location", User_locationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
