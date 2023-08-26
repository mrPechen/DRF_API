from typing import Any

from api.models import Musician
from api.serializers import MusicianSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@swagger_auto_schema(method='POST', request_body=MusicianSerializer)
@api_view(['GET', 'POST'])
def musicians_response(request: Any):
    musicians = Musician.objects.all()

    if request.method == 'GET':
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='PATCH', request_body=MusicianSerializer)
@api_view(['GET', 'PATCH', 'DELETE'])
def musician_response(request: Any, musician_pk: int):
    musician = get_object_or_404(Musician, pk=musician_pk)

    if request.method == 'GET':
        serializer = MusicianSerializer(musician)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = MusicianSerializer(musician, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
