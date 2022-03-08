from django.db import models

# Create your models here.

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH',
        SYNTH_POP = 'SP',
        ALTERNATIVE_ROCK = 'AR',
        REGGAE = 'RG',
        JAZZ = 'JZ',
        SOYOYO = 'SY',
        SEBEN = 'SB',
        ZINLI = 'ZL'
        AFROBEAT = 'AFB',

    name: CharField = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, null=True)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return self.name



class Listing(models.Model):
    title = models.fields.CharField(max_length=350)
    description = models.fields.TextField()
    created_at = models.fields.DateTimeField(auto_now_add=True)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
