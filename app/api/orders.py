from fastapi import APIRouter
from app.models.order_model import Order
from app.models.book_model import Book
from app.services import order_service


router = APIRouter()

@router.post("/")
def create_order(books: list[Book]):
    new_order = order_service.create_order(order_id=1, books=books)
    return {"message": "Commande créée avec succès", "order": new_order}
