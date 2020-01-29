from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('search', views.search_profiles, name= 'search_results'),
    path('accounts/profile/', views.user_profiles, name='profile'),
    path('profile/<str:username>', views.get_profile, name='profile_results'),
    path('chat/<username>', views.chating, name='chat'),

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)