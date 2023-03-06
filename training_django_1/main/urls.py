from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('sign_up', views.sign_up, name='sign_up'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
