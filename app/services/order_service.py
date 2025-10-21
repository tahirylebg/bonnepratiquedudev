"""
order_service.py — Logique métier pour la gestion des commandes.

Ce module gère la création et le traitement des commandes dans la boutique :
    -Calcule le prix total d’une commande.
    -Met à jour le stock des livres commandés.
    -Lève une erreur personnalisée (StockError) si un livre n’a plus de stock.

create_order : Crée une commande avec les livres fournis.
               Décrémente le stock de chaque livre.
               Lève une erreur StockError si un livre n'a plus de stock.

Ce service isole la logique métier afin que la couche API reste simple et claire
"""


from app.models.order_model import Order
from app.models.book_model import Book
from app.core.logging_config import get_logger
from app.core.errors import StockError  # on importe notre erreur personnalisée
from app.core.utils import format_price, current_timestamp



logger = get_logger()


def calculate_total(books):
    #Calcule le prix total d 'une commande
    total = sum(book.price for book in books)
    logger.debug(f"Calcul du total de commande : {total}€ pour {len(books)} livres")
    return total


def create_order(order_id: int, books: list[Book]):
    logger.info(f"Création d'une commande (id={order_id}) avec {len(books)} livres")

    total = calculate_total(books)

    for book in books:
        if book.stock > 0:
            book.stock -= 1
            logger.info(f"Stock mis à jour pour '{book.title}' → {book.stock} restants")
        else:
            # Ici, on lève une exception métier typée
            logger.error(f"Stock insuffisant pour le livre '{book.title}'")
            raise StockError(book.title)

    order = Order(id=order_id, books=books, total=total)
    logger.success(f"Commande créée avec succès (total={total}€)")
    return order
