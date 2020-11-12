from django.contrib       import admin
from django.contrib.admin import AdminSite
from .models              import Team, Teammitglied, Auftritt, Person


AdminSite.site_header = ""
AdminSite.site_title  = "Wiener Festwochen-Verwaltungstool"
AdminSite.


class Inline(admin.TabularInline):
    model = Team
    extra = 0


class BestellInline(admin.TabularInline):
    model = Teammitglied
    extra = 0


class TeamAdmin(admin.ModelAdmin):
    list_display =       ('id')
    list_display_links = ('id')
    ordering =      ['id']
    list_filter =   ['id']
    search_fields = ['id']
    fieldsets = [
        ('Fachbereichs-Daten', {'fields': [('KBEZ', 'LBEZ')]}),
        ('Detailinformation',  {'fields': ['Gebaeude'], 'classes': ['collapse']}),
    ]
    inlines = [TeamInline]


class TeammitgliedAdmin(admin.ModelAdmin):
    list_display =       ('id', 'Fachbereich', 'Stundenlohn')
    list_display_links = ('id', 'Fachbereich','Stundenlohn')
    ordering =      ['id']
    list_filter =   ['FS_id', 'FS_id']
    search_fields = ['Zuname']
    fieldsets = [
        ('HSL-Daten',         {'fields': [('Zuname', 'Vorname'), 'FS_KBEZ']}),
        ('Detailinformation', {'fields': ['Geburtstag']}),
    ]
    inlines = [BestellInline]


class AuftrittAdmin(admin.ModelAdmin):
    list_display =       ('id', 'Zeit')
    list_display_links = ('id', 'Zeit')
    ordering =      ['id']
    list_filter =   ['','Zeit']
    search_fields = ['Zeit']
    fieldsets = [
        ('Bier-Daten', {'fields': ['Bezeichnung', 'Sorte', 'Art']}),
        ('',           {'fields': ['Preis']}),
    ]
    inlines = [BestellInline]


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'FS_PNR', 'FS_BNR', "Menge",'Zeit')
    ordering =      ['-Zeit', '-id']
    list_filter =   ['Ort', 'Zeit']
    search_fields = ['Ort']
    fieldsets = [
        ('Bestell-Daten', {'fields': [('FS_PNR', 'FS_BNR', 'Menge')]}),
        ('',              {'fields': [('Ort', 'Zeit')]}),
    ]




admin.site.register(Team, TeamAdmin)
admin.site.register(Teammitglied, TeammitgliedAdmin)
admin.site.register(Auftritt, AuftrittAdmin)
admin.site.register(Person, PersonAdmin)