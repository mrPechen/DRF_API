from api.views import album_views, musician_views, song_views
from django.urls import path

urlpatterns = [
    path('musicians', musician_views.musicians_response),
    path('musicians/<int:musician_pk>/', musician_views.musician_response),
    path('musicians/<int:musician_pk>/albums', album_views.albums_actions),
    path('musicians/<int:musician_pk>/albums/<int:album_pk>', album_views.album_actions),
    path('musicians/<int:musician_pk>/albums/<int:album_pk>/songs', song_views.songs_actions),
    path('musicians/<int:musician_pk>/albums/<int:album_pk>/songs/<int:song_pk>', song_views.song_actions),
]
