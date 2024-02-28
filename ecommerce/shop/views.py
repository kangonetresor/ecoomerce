from django.shortcuts import render, HttpResponsePermanentRedirect, redirect
from .models import Product, Commande
# importation du module pour la pagination
from django.core.paginator import Paginator

# Create your views here.

# cette fonction a ete creer pour rendre le fichier index.html visible.
def index(request):
    product_object = Product.objects.all()
    # code pour le filtrage des recherches
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    # 
    # Pour la pagination
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    # 
    return render(request, 'shop/index.html', {'product_object': product_object})

def details(request, myid):  
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/details.html', {'product': product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode)
        com.save()
        return redirect('confirmation')


    return render(request, 'shop/checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html', {'name': nom})
 