from app.services import book_service
from app.models.book_model import Book

def seed():
    """Ajoute des livres de test dans la boutique."""
    books = [
        Book(id=1, title="1984", author="George Orwell", price=11.5, stock=8),
        Book(id=2, title="Le Meilleur des Mondes", author="Aldous Huxley", price=10.9, stock=5),
        Book(id=3, title="La Horde du Contrevent", author="Alain Damasio", price=15.2, stock=3),
        Book(id=4, title="Les Misérables", author="Victor Hugo", price=9.8, stock=10),
        Book(id=5, title="L'Étranger", author="Albert Camus", price=8.5, stock=12),
        Book(id=6, title="Harry Potter à l'école des sorciers", author="J.K. Rowling", price=13.7, stock=7),
        Book(id=7, title="Le Seigneur des Anneaux", author="J.R.R. Tolkien", price=18.9, stock=6),
        Book(id=8, title="Le Petit Prince", author="Antoine de Saint-Exupéry", price=7.5, stock=15),
        Book(id=9, title="Shining", author="Stephen King", price=12.9, stock=9),
        Book(id=10, title="Fondation", author="Isaac Asimov", price=13.3, stock=4),
        Book(id=11, title="Le Nom du Vent", author="Patrick Rothfuss", price=16.4, stock=5),
        Book(id=12, title="Neuromancien", author="William Gibson", price=11.2, stock=8),
        Book(id=13, title="Les Fleurs du mal", author="Charles Baudelaire", price=8.9, stock=6),
        Book(id=14, title="Le Parfum", author="Patrick Süskind", price=10.7, stock=7),
        Book(id=15, title="La Peste", author="Albert Camus", price=9.6, stock=9),
        Book(id=26, title="American Gods", author="Neil Gaiman", price=14.8, stock=5),
    ]
    for b in books:
        book_service.add_book(b)
    print("✅ Livres de test ajoutés !")

if __name__ == "__main__":
    seed()
