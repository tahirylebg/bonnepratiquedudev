"""
errors.py — Définit les exceptions personnalisées utilisées dans l'application.
Ces classes permettent de mieux identifier les erreurs métier.

BookNotFoundError : Erreur levée quand un livre demandé n'existe pas.

StockError : Erreur levée quand un livre n'a plus de stock disponible.
"""

class BookNotFoundError(Exception):
    def __init__(self, book_id: int):
        super().__init__(f"Livre introuvable (id={book_id})")
        self.book_id = book_id


class StockError(Exception):
    def __init__(self, title: str):
        super().__init__(f"Stock insuffisant pour le livre : {title}")
        self.title = title
