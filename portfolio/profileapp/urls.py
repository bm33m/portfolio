from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('profiles', views.profiles, name='profiles'),
    path('info', views.info, name='info'),
    path('edit', views.edit, name='edit'),
    path('deleteprofile', views.deleteProfile, name='deleteprofile'),
    path('delete', views.delete, name='delete'),
]
