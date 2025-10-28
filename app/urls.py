from django.contrib import admin
from django.urls import path
from genres.views import genre_list_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_list_view, name='genre-list'),
]
