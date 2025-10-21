"""
book_service.py c'est la logique métier pour la gestion des livres.
Ce module contient les fonctions qui implémentent la logique métier liée aux livres :
    -Récupérer tous les livres disponibles.
    -Rechercher un livre par son identifiant (ID).
    -Ajouter un nouveau livre à la base.

get_book : Cherche un livre dans la base en fonction de son identifiant.
           Si trouvé alors on log un message positif et on renvoie le livre.
           Sinon on log un avertissement (warning) et on renvoie None.
add_book : Reçoit un nouvel objet Book à ajouter.
           Enregistre un log avant et après l’ajout.
           Appelle la fonction db.add_book() pour sauvegarder le livre.
           Retourne l’objet ajouté.

Tout cela s'appuie sur :
    -la couche "base de données" (app/database/db.py) pour le stockage et la lecture,
    -le logger centralisé (app/core/logging_config.py) pour tracer les actions.

Ce service agit comme une interface entre l’API (app/api/books.py) et la base de données simulée,
assurant une architecture claire et modulaire.
"""

from app.models.book_model import Book
from app.database import db  #on importe notre "base de données"
from app.core.logging_config import get_logger

logger = get_logger()


def get_all_books():
    #Pour recuperer tout les livres disponibles
    logger.info("Récupération de tous les livres")
    return db.get_all_books()


def get_book(book_id: int):
    #Retourne un livre selon son ID.
    logger.info(f"Recherche du livre avec id={book_id}")
    book = db.get_book_by_id(book_id)
    if book:
        logger.info(f"Livre trouvé : {book.title}")
        return book
    logger.warning(f"Livre id={book_id} introuvable")
    return None


def add_book(book: Book):
    logger.info(f"Ajout du livre : {book.title}")
    db.add_book(book)
    logger.success(f"Livre ajouté avec succès : {book.title}")
    return book
