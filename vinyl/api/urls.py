import os
from django.contrib import admin
from django.urls import path, include
from vinyl.api.views import AlbumCreateView

urlpatterns = [
    path('albums/create/', AlbumCreateView.as_view(), name='album-create'),
]