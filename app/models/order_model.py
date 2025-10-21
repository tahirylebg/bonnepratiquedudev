from pydantic import BaseModel
from typing import List
from app.models.book_model import Book

class Order(BaseModel):
    id: int
    books: List[Book]
    total: float
