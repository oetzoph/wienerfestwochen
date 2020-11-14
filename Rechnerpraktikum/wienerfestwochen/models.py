from django.db import models
from django.utils import timezone


class Team(models.Model):
    id = models.IntegerField(blank=False, unique=True, primary_key=True, verbose_name='TeamID')

    def __str__(self):
        return self.id


class Teammitglied(models.Model):
    id = models.IntegerField(blank=False, unique=True, primary_key=True)
    Fachbereich = models.CharField(max_length=30, blank=False)
    Stundenlohn = models.DecimalField(max_digits=6, decimal_places=2, blank=False)

    def __str__(self):
        return self.Fachbereich + " " + self.Stundenlohn


class Person(models.Model):
    id = models.IntegerField(blank=False, unique=True, primary_key=True)
    PName = models.CharField(max_length=6, blank=False, default='Pils',
                             choices=[('Pils', 'Pils'), ('Bock', 'Bock'), ('Export', 'Export'), ('Weizen', 'Weizen'), ])
    ist_extern = models.BooleanField(default=False)
    Preis = models.IntegerField(default=5, blank=False, verbose_name='Preis pro Liter')

    def __str__(self):
        return self.Bezeichnung


class Auftritt(models.Model):
    FS_PNR = models.ForeignKey(Team, on_delete=models.PROTECT, blank=False, verbose_name='Besteller')
    id = models.IntegerField(blank=False, unique=True, primary_key=True)
    Zeit = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return ""
