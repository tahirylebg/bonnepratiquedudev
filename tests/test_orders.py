from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_order_does_not_update_stock():
    # On suppose qu'un livre existe avec stock > 0
    response = client.get("/books/1")
    book = response.json()
    old_stock = book["stock"]

    # Création d'une commande avec ce livre
    client.post("/orders", json=[book])

    # On relit le livre
    response_after = client.get("/books/1")
    new_stock = response_after.json()["stock"]

    # Le stock devrait diminuer, mais ne change pas -> bug
    assert new_stock == old_stock, "Le stock n’a pas été mis à jour (bug logique simulé)"
