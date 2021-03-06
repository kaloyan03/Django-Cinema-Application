"""cinema_app URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cinema_app.tickets_cart import signals

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('movies/', include('cinema_app.movies.urls')),
                  path('auth/', include('cinema_app.cinema_auth.urls')),
                  path('profile/', include('cinema_app.profiles.urls')),
                  path('cart/', include("cinema_app.tickets_cart.urls")),
                  path('projections/', include("cinema_app.projections.urls")),
                  path('', include('cinema_app.landing_page.urls')),
                  path('ratings/', include('star_ratings.urls', namespace='ratings')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
