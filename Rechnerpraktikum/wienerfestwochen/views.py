from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from .models import Team, Teammitglied, Auftritt, Person
from .forms import FBForm, HSLForm, BierForm, BestellungForm


# Allgemeines Schema für Programmlogik:
# **************************************
#
# def Auswertung_view(request):
#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':
#        # create a form instance and populate it with data from the request:
#        form = NameForm(request.POST)
#        # check whether it's valid:
#        if form.is_valid():
#            # process the data in form.cleaned_data as required
#            # ...
#            # redirect to a new URL:
#            return HttpResponseRedirect('/Auswertung/')
#    # if a GET (or any other method) we'll create a blank form
#    else:
#        form = NameForm()
#    return render(request, 'Bier/Auswertung.html', {'form': form})


def index(request):
    return render(request, 'Bier/base.html')


def Person_view(request):
    if request.method == 'POST':
        form = FBForm(request.POST)
        if form.is_valid():
            form.save()
            form = FBForm()
            fbs = FB.objects.filter().order_by('LBEZ')
    else:
        fbs = FB.objects.filter().order_by('LBEZ')
        form = FBForm()
    args = {}
    args['form'] = form
    args['fbs'] = fbs
    return render(request, 'Bier/FB.html', args)


def Team_view(request):
    if request.method == 'POST':
        form = HSLForm(request.POST)
        if form.is_valid():
            form.save()
            form = HSLForm()
            hsls = HSL.objects.filter().order_by('Zuname', 'Vorname')
    else:
        hsls = HSL.objects.filter().order_by('Zuname', 'Vorname')
        form = HSLForm()
    args = {}
    args['form'] = form
    args['hsls'] = hsls
    return render(request, 'Bier/HSL.html', args)


def Teammitglied_view(request):
    if request.method == 'POST':
        form = BierForm(request.POST)
        if form.is_valid():
            form.save()
            form = BierForm()
            biere = Bier.objects.filter().order_by('Bezeichnung')
    else:
        biere = Bier.objects.filter().order_by('Bezeichnung')
        form = BierForm()
    args = {}
    args['form'] = form
    args['biere'] = biere
    return render(request, 'Bier/Bier.html', args)


def Auftriit_view(request):
    if request.method == 'POST':
        form = BestellungForm(request.POST)
        if form.is_valid():
            form.save()
            form = BestellungForm()
            bestellungs = Bestellung.objects.filter().order_by('-id').annotate(Wert=F('Menge') * F('FS_BNR__Preis'))
            print(bestellungs)
    else:
        bestellungs = Bestellung.objects.filter().order_by('-id').annotate(Wert=F('Menge') * F('FS_BNR__Preis'))
        print(bestellungs)
        form = BestellungForm()
    args = {}
    args['form'] = form
    args['bestellungs'] = bestellungs
    return render(request, 'Bier/Bestellungen.html', args)

