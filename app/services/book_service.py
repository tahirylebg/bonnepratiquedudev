from app.models.book_model import Book
from app.database import db  #on importe notre "base de données"
from app.core.logging_config import get_logger

logger = get_logger()


def get_all_books():
    logger.info("Récupération de tous les livres")
    return db.get_all_books()


def get_book(book_id: int):
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
