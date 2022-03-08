from django import forms
from .models import *


class ContactUsForm(forms.Form):
   name = forms.CharField(max_length=100,empty_value='')
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


class BandForm(forms.ModelForm):
   class Meta:
     model = Band
     fields = '__all__'
     #exclude = ('active', 'official_homepage')  # ajoutez cette ligne pour esclure certains champs



class ListingForm(forms.ModelForm):
   class Meta:
     model = Listing
     fields = '__all__'