from django.contrib import admin
from .models import Category, Product, Commande

admin.site.site_header = "Sami shop Page d'administration"
admin.site.index_title = "Gestionnaire"
admin.site.site_title = "SamiShop Administrator"

# Register your models here.
# Affichage des informations sous forme de tableau
class Admincategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class Adminproduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price',)

class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'ville', 'pays','total', 'zipcode', 'date_commande')

# Ajout des classe du fichier models.py a l'espace de l'administrateur.
admin.site.register(Category, Admincategorie)
admin.site.register(Product, Adminproduct)
admin.site.register(Commande, AdminCommande)