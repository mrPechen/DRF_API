from typing import Any

from api.models import Album
from api.serializers import AlbumSerializer, PatchAlbumSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@swagger_auto_schema(method='POST', request_body=AlbumSerializer)
@api_view(['GET', 'POST'])
def albums_actions(request: Any, musician_pk: int):
    albums = Album.objects.filter(musician=musician_pk).all()

    if request.method == 'GET':
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='PATCH', request_body=PatchAlbumSerializer)
@api_view(['GET', 'PATCH', 'DELETE'])
def album_actions(request: Any, musician_pk: int, album_pk: int):
    album = get_object_or_404(Album, musician=musician_pk, pk=album_pk)
    response_serializer = AlbumSerializer(album)

    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = PatchAlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
