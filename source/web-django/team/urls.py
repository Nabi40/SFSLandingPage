from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OurTeamViewSet,
    HeadViewSet,
    HeadTeamViewSet,
    AllTeamDescripViewSet,
    AllTeamViewSet
)

router = DefaultRouter()
router.register(r'our-team', OurTeamViewSet)
router.register(r'head', HeadViewSet)
router.register(r'head-team', HeadTeamViewSet)
router.register(r'all-team-descrip', AllTeamDescripViewSet)
router.register(r'all-team', AllTeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
