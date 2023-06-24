"""
URL configuration for NEWSPAPER1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # third party urls
    path('summernote/', include('django_summernote.urls')),
    
    # built in customized urls
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    
    # custom urls
    path("", include("newspaper1_app.urls")),
    path("api/v1/", include("api_app.urls")),
    
]


if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    
handler404 = "newspaper1_app.views.handler404"