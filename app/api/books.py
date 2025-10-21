from fastapi import APIRouter, HTTPException
from app.models.book_model import Book
from app.services import book_service


router = APIRouter()


@router.get("/")
def list_books():
    return book_service.get_all_books()


@router.get("/{book_id}")
def get_book(book_id: int):
    book = book_service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Livre introuvable")
    return book


@router.post("/")
def create_book(book: Book):
    """Ajoute un nouveau livre à la boutique."""
    new_book = book_service.add_book(book)
    return {
        "message": "Livre ajouté avec succès",
        "book": new_book.model_dump()
    }
