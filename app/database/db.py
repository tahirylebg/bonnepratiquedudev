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