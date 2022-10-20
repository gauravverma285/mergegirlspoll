"""mergeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from django.conf.urls import include

from django.urls import path, include #1
from django.views.generic.base import TemplateView

from blog import views

from django.conf import settings
from django.conf.urls.static import static
from blog.views import ChangePasswordView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', include('blog.urls')),
    # path('signup/', views.sign_up),
    

    path("", TemplateView.as_view(template_name="home.html"), name="home"), #1
    # path("", TemplateView.as_view(template_name="login.html"), name="login"),
    
    path("blog/", include("blog.urls")),
    path("blog/", include("django.contrib.auth.urls")),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
