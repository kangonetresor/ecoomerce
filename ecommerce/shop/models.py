from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added'] #Permet de mettre les elements recement ajouter a la premiere ligne
    # cette fonction nous permet d'avoir le nom de la categorie qui est retourner au noiveau de la BD et autre
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name = 'categorie', on_delete=models.CASCADE) #CASCADE permet en cas de suppression de ne pas affeceter l'autre classe
    #On veut ici ajouter les images mais on va le faire en ligne
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)
    # comme on veut classer les produit par ordre d'ajout on va faire la chose suivante : 
    class Meta:
        ordering = ['-date_added'] 
    # cette fonction nous permet d'avoir le nom du produit qui est retourner au noiveau de la BD et autre
    def __str__(self):
        return self.title
    
class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    ville = models.CharField(max_length=300)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.nom

    