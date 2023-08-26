from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя исполнителя')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название альбома')
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name='Имя исполнителя')
    year_of_release = models.PositiveIntegerField(verbose_name='Год выпуска альбома')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название песни')
    number_in_album = models.PositiveIntegerField(verbose_name='Порядковый номер в альбоме')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом')

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        constraints = [
            models.UniqueConstraint(name='uniq album number', fields=['album', 'number_in_album'])
        ]

    def __str__(self):
        return self.name
