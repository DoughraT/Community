from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_service', views.add_service, name="add-service"),
    path('search_providers', views.search_providers, name="search-providers"),
    path('provider_profile/<provider_id>', views.provider_profile, name="provider-profile"),
]