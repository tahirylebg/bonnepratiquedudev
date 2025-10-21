from app.services import book_service
from app.models.book_model import Book

def seed():
    """Ajoute des livres de test dans la boutique."""
    books = [
        Book(id=10, title="Fahrenheit 451", author="Ray Bradbury", price=12.5, stock=4),
        Book(id=11, title="Dune", author="Frank Herbert", price=14.0, stock=6),
    ]
    for b in books:
        book_service.add_book(b)
    print("✅ Livres de test ajoutés !")

if __name__ == "__main__":
    seed()
