from django.db import models
from django.utils import timezone


class Produktion(models.Model):
    id = models.IntegerField(blank=False, unique=True, primary_key=True)
    Titel = models.CharField(max_length=50, blank=False)
    Typ = models.CharField(max_length=7, default='Theater', choices=[('Theater', 'Theater'), ('Tanz', 'Tanz'), ('Musik', 'Musik')])
    Dauer = models.IntegerField(blank=False)
    Leitung = models.CharField(max_length=50, blank=False)
    Sprache = models.CharField(max_length=30)
    hat_Untertitel = models.BooleanField(default=False)

    def __str__(self):
        return self.Titel


class Team(models.Model):
    id = models.IntegerField(blank=False, unique=True, primary_key=True, verbose_name='TeamID')
    FS_ProduktionID = models.ForeignKey(Produktion, on_delete=models.PROTECT, blank=False, verbose_name='ID der Produktion')

    def __str__(self):
        return self.id


class Person(models.Model):
    id = models.IntegerField(blank=False, unique=True, primary_key=True)
    PName = models.CharField(max_length=100, blank=False, verbose_name='Name')
    ist_extern = models.BooleanField(default=False)

    def __str__(self):
        return self.PName


class Teammitglied(models.Model):
    id = models.IntegerField(blank=False, unique=True, primary_key=True)
    Fachbereich = models.CharField(max_length=12, blank=False, choices=[('Dramaturgie', 'Dramaturgie'), ('Performer', 'Performer'), ('Organisation', 'Organisation'), ('Bühne', 'Bühne'), ('Ton', 'Ton')])
    Stundenlohn = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    FS_TeamID = models.ForeignKey(Team, on_delete=models.PROTECT, blank=False, verbose_name='ID des Teams')
    FS_PersonID = models.ForeignKey(Person, on_delete=models.PROTECT, blank=False, verbose_name='ID der Person')

    def __str__(self):
        return self.id + ", " + self.Fachbereich


class Auftritt(models.Model):
    id = models.IntegerField(blank=False, unique=True, primary_key=True)
    Zeit = models.DateTimeField(default=timezone.now, blank=False, verbose_name="Beginn des Auftritts")
    FS_TeamID = models.ForeignKey(Team, on_delete=models.PROTECT, blank=False, verbose_name='ID des Teams')

    def __str__(self):
        return self.id + ", " + self.Zeit
