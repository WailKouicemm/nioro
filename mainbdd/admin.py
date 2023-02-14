from django.contrib import admin
from .models import *

admin.site.register(Utilisateur)
admin.site.register(Jour)
admin.site.register(Magasin)
admin.site.register(Horeur)
admin.site.register(Categorie)
admin.site.register(Publication)
admin.site.register(Service)
admin.site.register(ServiseNonDispo)
