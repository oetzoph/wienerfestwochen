from django import forms
from .models import Team, Person, Teammitglied, Produktion



class ProduktionForm(forms.ModelForm):
	class Meta:
		model = Produktion
		fields = ('id', 'Titel', 'Typ', 'Dauer', 'Leitung', 'Sprache', 'hat_Untertitel')


class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ('id', 'FS_ProduktionID')


class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('id', 'PName', 'ist_extern')


class TeammitgliedForm(forms.ModelForm):
	class Meta:
		model = Teammitglied
		fields = ('id', 'Fachbereich', 'Stundenlohn', 'FS_TeamID', 'FS_PersonID')
