from typing import Any

from api.models import Song
from api.serializers import PatchSongSerializer, SongSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@swagger_auto_schema(method='POST', request_body=SongSerializer)
@api_view(['GET', 'POST'])
def songs_actions(request: Any, musician_pk: int, album_pk: int):
    songs = Song.objects.filter(album=album_pk).all()

    if request.method == 'GET':
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='PATCH', request_body=PatchSongSerializer)
@api_view(['GET', 'PATCH', 'DELETE'])
def song_actions(request: Any, musician_pk: int, album_pk: int, song_pk: int):
    song = get_object_or_404(Song, album=album_pk, pk=song_pk)
    response_serializer = SongSerializer(song)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = PatchSongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
