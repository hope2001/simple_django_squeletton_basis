"""merchex URL Configuration

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
from listings import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('bands/', views.band_list , name='band_list'),
                  path('bands/<int:band_id>/', views.band_detail, name='band_details'),
                  path('bands/add/', views.band_add , name='band_add'),
                  path('bands/<int:band_id>/update/', views.band_upd, name='band_upd'),
                  path('about/', views.about),
                  path('listing/', views.listing, name='listing_list'),
                  path('listing_details/<int:listing_id>', views.listing_details, name='listing_details'),
                  path('listing/add/', views.listing_add, name='listing_add'),
                  path('listing/<int:listing_id>/update', views.listing_upd, name='listing_upd'),
                  path('annonces/', views.annonces, name='annonces'),
                  path('contact/', views.contact, name ='contact_us'),
                  path('contact-success-send/', views.email_sent, name ='email-sent')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)