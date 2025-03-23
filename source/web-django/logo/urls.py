from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import logoViewSet

router = DefaultRouter()
router.register(r'logo', logoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
