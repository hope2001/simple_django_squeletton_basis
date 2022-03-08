from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactUsForm

from .forms import BandForm, ListingForm
from .models import *

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/brand_list.html', {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id = band_id)

    return render(request, 'listings/band_detail.html', {'band': band})

def band_add(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band_details', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/new_band.html', {'form': form})



def band_upd(request, band_id):
    band = Band.objects.get(id = band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance= band)
        if form.is_valid():
            band = form.save()
            return redirect('band_details', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})




def about(request):
    return HttpResponse('<h1> A propos de nous </h1> <p> contenu de la page à propos de nous </p>')

def listing(request):
    listings= Listing.objects.all()
    return render(request,'listings/listing.html',{'listings': listings})

def listing_details(request, listing_id):
    listing= Listing.objects.get(id=listing_id)
    return render(request,'listings/listing_details.html',{'listing': listing})

def listing_add(request):

    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return render(request, 'listings/listing_details.html',{'listing': listing})
    else:
        form = ListingForm()

    return render(request,'listings/new_listing.html',{'form': form})


def listing_upd(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    if request.method  == 'POST':
        form = ListingForm(request.POST, instance= listing)
        if form.is_valid():
            form.save()
            return redirect('listing_details', listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request, 'listings/listing_update.html', {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band_list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})


def annonces(request):
    return HttpResponse('<h1> Annonces</h1>')

def email_sent(request):
    val = 1
    return render(request, 'listings/brand_list.html', {'val': val})

def contact(request):
   # print('La méthode de requête est : ', request.method)
   # print('Les données POST sont : ', request.POST)
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request,'listings/contact.html', {'form': form})
