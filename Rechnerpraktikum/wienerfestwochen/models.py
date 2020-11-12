from django.db import models
from django.utils import timezone


class Team(models.Model):
    id = models.IntegerField(max_length=4, blank=False, unique=True, verbose_name='TeamID')
    FS_id =

    def __str__(self):
        return self.id


class Teammitglied(models.Model):
    id = models.IntegerField(max_length=30, blank=False)
    Fachbereich = models.CharField(max_length=30, blank=False)
    Stundenlohn = models.DateField(default=timezone.now(), blank=True)

    def __str__(self):
        return self.Fachbereich + " " + self.Stundenlohn


class Person(models.Model):
    id = models.IntegerField(max_length=30, blank=False)
    PName = models.CharField(max_length=6, blank=False, default='Pils',
                             choices=[('Pils', 'Pils'), ('Bock', 'Bock'), ('Export', 'Export'), ('Weizen', 'Weizen'), ])
    ist_extern = models.BooleanField(max_length=2, blank=False',choices=
                           choices=[('Obergärig', 'Obergärig'), ('Untergärig', 'Untergärig'), ])
    Preis = models.IntegerField(default=5, blank=False, verbose_name='Preis pro Liter')

    def __str__(self):
        return self.Bezeichnung


class Auftritt(models.Model):
    FS_PNR = models.ForeignKey(Team, on_delete=models.PROTECT, blank=False, verbose_name='Besteller')
    id = models.IntegerField(default=1, blank=False)
    Zeit = models.DateTimeField(default=timezone.now(), blank=False)

    def __str__(self):
        return ""
