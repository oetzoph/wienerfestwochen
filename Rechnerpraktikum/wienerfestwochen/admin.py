from django.contrib       import admin
from django.contrib.admin import AdminSite
from .models              import Teammitglied, Auftritt, Person, Produktion


AdminSite.site_header = ""
AdminSite.site_title  = "Wiener Festwochen-Verwaltungstool"
AdminSite.sit_title = "Verwaltung"





class BestellInline(admin.TabularInline):
    model = Teammitglied
    extra = 0





class TeammitgliedAdmin(admin.ModelAdmin):
    list_display =       ('TMID', 'Fachbereich', 'Stundenlohn')
    list_display_links = ('TMID', 'Fachbereich','Stundenlohn')
    ordering =      ['TMID']
    list_filter =   ['FS_PID', 'FS_PID']
    search_fields = ['Fachbereich']
    fieldsets = [
        ('Fachbereichsdaten',         {'fields': ['Fachbereich']}),
        ('Stundenlohndaten', {'fields': ['Stundenlohn']}),
    ]
    inlines = [BestellInline]


class AuftrittAdmin(admin.ModelAdmin):
    list_display =       ('AuftrittiD', 'Zeit', 'FS_TID')
    list_display_links = ('AuftrittiD', 'Zeit', 'FS_TID')
    ordering =      ['AuftrittiD']
    list_filter =   ['Zeit']
    search_fields = ['Auftrittid']
    fieldsets = [
        ('Auftrittdaten', {'fields': ['Beginn des Auftritts']}),

    ]
    inlines = [BestellInline]


class PersonAdmin(admin.ModelAdmin):
    list_display = ('PID', 'Pname', 'ist_extern')
    ordering =      ['PID', 'PID']
    list_filter =   ['Pname', 'Pname']
    search_fields = ['Pname','PID']
    fieldsets = [
        ('Personen-Daten', {'fields': [('PID', 'Pname', 'ist_extern','FS_TID')]}),

    ]
class ProduktionAdmin(admin.ModelAdmin):
    list_display =       ('Produktionid', 'Titel','Leitung')
    list_display_links = ('Produktionid', 'Titel','Leitung')
    ordering =      ['Produktionid']
    list_filter =   ['Produktionid','Titel','Leitung']
    search_fields = ['Produktionid','Titel','Leitung']
    fieldsets = [
        ('Produktionsdaten', {'fields': ['Produktionid', 'Titel', 'Leitung']}),

    ]
    inlines = [BestellInline]



admin.site.register(Team, TeamAdmin)
admin.site.register(Teammitglied, TeammitgliedAdmin)
admin.site.register(Auftritt, AuftrittAdmin)
admin.site.register(Person, PersonAdmin)