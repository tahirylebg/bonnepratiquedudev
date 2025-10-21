"""
books.py c'est la Routes API liées à la gestion des livres.

Ce module définit les endpoints FastAPI permettant d’interagir avec la "boutique de livres" :
    -  GET /books/ → Liste tous les livres qui sont disponibles .
    -  GET /books/{book_id} → Récupère un livre précis selon son ID.
    -  POST /books/ → Ajoute un nouveau livre à la base .

Un endpoint : adresse (route) que notre application expose pour que
les utilisateurs ou les autres programmes puissent interagir avec elle.

Il s’appuie sur :
- book_model
- book_service (logique métier : lecture, ajout, recherche).

Chaque route est documentée avec une docstring courte, et renvoie des réponses JSON.
Les erreurs sont gérées via `HTTPException` avec des statuts explicites (ex. 404).

Dans ce fichier :

get_book : book=book_service.get_book(book_id) -> Va chercher le livre qui correspond à cet identifiant (book_id)
           dans la base de données (ou la simulation de base).
           si ont ne le trouve pas , le livre est donc introuvable sinon il retourne le livre
create_book : Ajoute un nouveau livre à la boutique.

"""

from fastapi import APIRouter, HTTPException
from app.models.book_model import Book
from app.services import book_service


router = APIRouter()


@router.get("/")
def list_books():
    #Retourne la liste de tous les livres disponibles
    return book_service.get_all_books()


@router.get("/{book_id}")
def get_book(book_id: int):
    #Retourne un livre spécifique selon son ID.
    book = book_service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Livre introuvable")
    return book


@router.post("/")
def create_book(book: Book):
    new_book = book_service.add_book(book)
    return {
        "message": "Livre ajouté avec succès",
        "book": new_book.model_dump()
    }
