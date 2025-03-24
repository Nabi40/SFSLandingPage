from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import aboutUssViewSet

router = DefaultRouter()
router.register(r'aboutUss', aboutUssViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
