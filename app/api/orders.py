
"""
📦 orders.py c'est la routes API liées à la gestion des commandes.

Ce module définit les endpoints FastAPI permettant de créer et manipuler des commandes clients.
Actuellement, il contient une seule route principale :
    POST /orders/ → Crée une nouvelle commande à partir d’une liste de livres.

Comment ca fonctionne :
1️ - Le client envoie une liste de livres (instances de `Book`) à commander.
2️ - L’API appelle le service `order_service.create_order()` qui :
    - calcule le total,
    - décrémente le stock,
    - crée un objet `Order` complet.
3- La commande est renvoyée dans la réponse avec un message de succès.

Ce fichier appartient à la couche **API** : il expose les routes HTTP.
La logique métier est isolée dans `app/services/order_service.py`.

"""


from fastapi import APIRouter
from app.models.order_model import Order
from app.models.book_model import Book
from app.services import order_service


router = APIRouter()

@router.post("/")
def create_order(books: list[Book]):
    new_order = order_service.create_order(order_id=1, books=books)
    return {"message": "Commande créée avec succès", "order": new_order}
