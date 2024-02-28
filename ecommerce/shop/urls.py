# dans se fichier nous allons mettre les urls de notre application cela va permettre a notre projet d'etre porter au sein d'un autre plus grand sans causer de probleme. (reutilisabilite)
from django.urls import path
from shop.views import index, details, checkout, confirmation


# from shop.views import index

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', details, name="details"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation"),
]

