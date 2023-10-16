from django.urls import path
from .views import *

urlpatterns = [
    path('api/who_are_we/list/', WhoAreWeList.as_view(), name='who-are-we-list'),
    path('api/who_are_we/details/<int:pk>/', WhoAreWeDetail.as_view(), name='who-are-we-detail'),
    path('api/featured/images/', FeaturedImageList.as_view(), name='featured-image-list'),
    path('api/featured/images/<int:pk>/', FeaturedImageDetail.as_view(), name='featured-image-detail'),
    path('api/certifications/', CertificationList.as_view(), name='certification-list'),
    path('api/certifications/<int:pk>/', CertificationDetail.as_view(), name='certification-detail'),
    path('api/social_responsibility/', SocialResponsibilityList.as_view(), name='certification-list'),
    path('api/social_responsibility/<int:pk>/', SocialResponsibilityDetail.as_view(), name='certification-detail'),
    path('api/social_media_urls/', SocialMediaURLList.as_view(), name='social-media-url-list'),
    path('api/social_media_urls/<int:pk>/', SocialMediaURLDetail.as_view(), name='social-media-url-detail'),


]
