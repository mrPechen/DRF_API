from api.models import Album, Musician, Song
from rest_framework import serializers


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['id', 'name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'musician', 'year_of_release']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'number_in_album', 'album']


class PatchSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['name']


class PatchAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name']
