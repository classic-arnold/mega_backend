"""
mega_backend URL Configuration

The `urlpatterns` list routes URLs to views
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from core import views as core_views, urls as core_urls

from accounts import views as accounts_views, urls as accounts_urls

from developer import urls as developer_urls

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import RedirectView

# DRF router configuration

api_router = routers.DefaultRouter()
api_router.register(r'community-types', core_views.CommunityTypeViewSet, basename='community_type')
api_router.register(r'profiles', accounts_views.ProfileViewSet, basename='profile')
api_router.register(r'features', core_views.FeatureViewSet, basename='feature')
api_router.register(r'communities', core_views.CommunityViewSet, basename='community')

# the urls

urlpatterns = [
    path('api/', include(core_urls)),
    path('api/', include(api_router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('accounts/', include(accounts_urls)),
    path('developer/', include(developer_urls)),
    path('favicon.ico', RedirectView.as_view(url='/static/core/img/favicon.ico')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
