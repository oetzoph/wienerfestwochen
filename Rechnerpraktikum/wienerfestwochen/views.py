from django.shortcuts import render
from .models import Produktion, Team, Person, Teammitglied
from .forms import ProduktionForm, TeamForm, PersonForm, TeammitgliedForm


def dialog1(request):
		return render(request, "dialog1.html", {})

def index(request):
    return render(request, 'wienerfestwochen/base.html')

def Produktion_view(request):
	if request.method == 'POST':
		form = ProduktionForm(request.POST)
		if form.is_valid():
			form.save()
			form = ProduktionForm()
			prods = Produktion.objects.filter().order_by('Titel')
	else:
		prods = Produktion.objects.filter().order_by('Titel')
		form = ProduktionForm()
	args = {}
	args['form'] = form
	args['prods'] = prods
	return render(request, 'wienerfestwochen/Produktion.html', args)
