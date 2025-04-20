from django.urls import path
from .views import reference_create_api, reference_list_api, another_model_create_api, another_model_list_api

urlpatterns = [
    path('', reference_create_api, name='reference-create'),
    path('', reference_list_api, name='reference-list'),
    path('', another_model_create_api, name='another-model-create'),
    path('', another_model_list_api, name='another-model-list'),
]
