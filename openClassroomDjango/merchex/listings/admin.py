from django.contrib import admin
from .models import *


# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


class AnnoncesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'band')


admin.site.register(Band, BandAdmin)

admin.site.register(Listing, AnnoncesAdmin)
