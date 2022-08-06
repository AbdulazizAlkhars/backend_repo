"""travelapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from trip import views

from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from trip import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("register/", views.UserCreateAPIView.as_view(), name="register"),
    path("profile/", views.UserProfileCreateAPIView.as_view(), name="Profile Creation"),
    path("trip/create/", views.TripCreateAPIView.as_view(), name="Create Trip"),
    path("trip/<int:trip_id>/", views.TripUpdateAPIView.as_view(), name="Trip Update"),
    path("trip/<int:trip_id>/delete/", views.TripDeleteAPIView.as_view(), name="Trip Delete"),
    path("trip/", views.TripListAPIView.as_view(), name="Trip List"),
    path("usertrip/<int:user_id>/", views.UserTripListAPIView.as_view(), name="User Trip List"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
