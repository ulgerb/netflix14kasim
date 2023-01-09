from django.contrib import admin
from .models import *
# Register your models here.


class ProfilAdmin(admin.ModelAdmin):

    list_display = ('user','name', 'pinon','id')
    


admin.site.register(Profil,ProfilAdmin)
admin.site.register(Video)