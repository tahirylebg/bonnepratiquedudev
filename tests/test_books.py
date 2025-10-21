from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_book():
    new_book = {
        "id": 3,
        "title": "L'Étranger",
        "author": "Albert Camus",
        "price": 9.99,
        "stock": 4
    }
    response = client.post("/books", json=new_book)
    assert response.status_code == 200
    data = response.json()
    assert data["book"]["title"] == "L'Étranger"

    # Vérifie que le livre a bien été ajouté
    list_response = client.get("/books")
    titles = [book["title"] for book in list_response.json()]
    assert "L'Étranger" in titles

def test_get_book_not_found():
    response = client.get("/books/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Livre introuvable"


