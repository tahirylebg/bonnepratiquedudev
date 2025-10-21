"""
utils.py : Fonctions utilitaires génériques de l'application.
Elles améliorent la lisibilité et évitent la duplication de code.

format_price : Formate un prix en euros avec deux décimales

current_timestamp : Retourne l'horodatage actuel au format lisible.

find_by_id : Recherche un élément par son identifiant dans une liste d'objets avec attribut 'id'.
             Tout d'abord , on parcourt chaque livre dans la liste, sachant que
             getattr(item, "id", None) essaie de lire la propriété id de l’objet item , si ce qu'on
             essaie de lire est égale à l'identifiant qu'on cherche donc on a trouvé l'objet.
             Sinon on retourne None , parce ca veut dire qu'il n'existe pas.

"""

from datetime import datetime


def format_price(price: float) -> str:
    return f"{price:.2f} €"

def current_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def find_by_id(items: list, item_id: int):
    for item in items:
        if getattr(item, "id", None) == item_id:
            return item
    return None
