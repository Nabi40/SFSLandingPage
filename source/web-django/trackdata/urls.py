from django.urls import path
from .views import track_visit_api

urlpatterns = [
    path('track-visit/', track_visit_api, name='track-visit'),
]
