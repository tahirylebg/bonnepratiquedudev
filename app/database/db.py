"""
db.py — Simulation d'une base de données en mémoire.
Cette couche isole la logique de stockage pour faciliter l'évolution future (ex : passage à SQLite ou PostgreSQL).

load_books : Si le fichier books.json existe → on charge les livres sauvegardés.
               *open(DB_FILE, "r", encoding="utf-8") sert à ouvrir le fichier JSON en mode lecture ("r")
                avec l’encodage UTF-8, pour pouvoir lire correctement son contenu texte (y compris les accents)
            sinon on initialise une petite base par défaut avec les livres qu'on veut y mettre.
            Les données sont transformées en objets Book grâce à Book(**b).

save_book : Il sert de sauvegarde persistante , il convertit tous les objets Book en dictionnaires (model_dump())
            il les écrit dans books.json au format JSON lisible et indenté
            et persiste les ajouts même après redémarrage .

get_all_book : Renvoie tous les livres.

get_book_by_id : Cherche dans la liste BOOKS_DB le livre dont l’identifiant (id) est égal à book_id.
                 Si un livre correspond alors il renvoie ce livre.
                 Sinon il renvoie None

add_book : Ajoute un nouveau livre (book) dans la liste des livres (BOOKS_DB) grace à BOOKS_DB.append(book)
           enregistre la nouvelle liste dans le fichier JSON grace à save_books(),puis renvoie le livre ajouté

reset_books_db(): Réinitialise la base .

"""


import json
from pathlib import Path
from app.models.book_model import Book

DB_FILE = Path(__file__).parent / "books.json"

print(f"📁 books.json sera enregistré dans : {DB_FILE.resolve()}")


def load_books():
    if DB_FILE.exists():
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book(**b) for b in data]
    return [
        Book(id=1, title="1984", author="George Orwell", price=10.99, stock=5),
        Book(id=2, title="Le Petit Prince", author="Antoine de Saint-Exupéry", price=8.50, stock=3)
    ]

BOOKS_DB = load_books()

def save_books():
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump([b.model_dump() for b in BOOKS_DB], f, ensure_ascii=False, indent=2)

def get_all_books() -> list[Book]:
    return BOOKS_DB

def get_book_by_id(book_id: int) -> Book | None:
    for book in BOOKS_DB:
        if book.id == book_id:
            return book
    return None

def add_book(book: Book) -> Book:
    BOOKS_DB.append(book)
    save_books()
    return book

def reset_books_db():
    global BOOKS_DB
    BOOKS_DB = []