from django.db import models
from django.utils import timezone





class Produktion(models.Model):
    Produktionid = models.IntegerField(max_length=30, blank=False, unique=True, verbose_name='Produktion')
    Titel = models.IntegerField(max_length=30, blank=False, verbose_name= "Titel")
    Leitung = models.CharField(max_length=30, blank=False, verbose_name= 'Leitung')

class Person(models.Model):
    PID = models.IntegerField(max_length=30, blank=False, unique=True)
    PName = models.CharField(max_length=30, blank=False)

    ist_extern = models.BooleanField(max_length=2, blank=False,
                           choices=[('JA', 'JA'), ('Nein', 'Nein'), ])

    def __str__(self):
        return self.Pname

class Team(models.Model):
    Teamid = models.IntegerField(max_length=4, blank=False, unique=True, verbose_name='Teamid')
    FS_PR = models.ForeignKey(Produktion, on_delete=models.PROTECT, blank=False)

class Teammitglied(models.Model):
    TMID = models.IntegerField(max_length=30, blank=False, unique=True, verbose_name='id')
    Fachbereich = models.CharField(max_length=30, blank=False)
    Stundenlohn = models.IntegerField(max_length=30, blank=True, verbose_name='Stundenlohn')
    FS_TID = models.ForeignKey(Team, on_delete=models.PROTECT, blank=False)
    FS_PID = models.ForeignKey(Person, on_delete=models.PROTECT, blank=False)
    def __str__(self):
        return self.Fachbereich + " " + self.Stundenlohn


class Auftritt(models.Model):
    FS_TID = models.ForeignKey(Team, on_delete=models.PROTECT, blank=False, verbose_name='Auftritt')
    AuftrittID = models.IntegerField(max_length=30, blank=False, unique=True)
    Zeit = models.DateTimeField(default=timezone.now(), blank=False)

    def __str__(self):
        return



