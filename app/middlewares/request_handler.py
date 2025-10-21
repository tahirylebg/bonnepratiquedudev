"""
request_logger.py est un middleware de journalisation des requêtes HTTP.

Ce module intercepte toutes les requêtes et réponses HTTP de l’application FastAPI pour en faire un suivi complet dans les logs :
    -Affiche la méthode (GET, POST, etc.) avec l’URL appelée.
    -Enregistre le code de réponse renvoyé (ex : 200, 404, 500...).
    -Permet de retracer le parcours complet d’une requête pour le diagnostic et le débogage.

Starlette est la base “serveur web asynchrone” sur laquelle FastAPI est construit.
FastAPI ajoute juste la validation, la documentation et les outils de développement modernes.

get_logger() : récupère ton logger personnalisé défini dans logging_config.py.
logger servira à enregistrer les informations sur chaque requête et réponse.

On déclare une classe qui hérite de BaseHTTPMiddleware.
Ce middleware va s’exécuter automatiquement à chaque requête qui passe par notre application.
A l'interieur , avant de traiter la requête, on log la méthode HTTP (GET, POST, etc.) ,l'URL appelée (/books/, /orders/, etc.)
Puis , on laisse la requête continuer son chemin vers la route correspondante (ou un autre middleware).
(response ) contient la réponse que l'API renvoie.
Après la réponse, on log :
    Le code HTTP (200, 404, 500, etc.) et l’URL correspondante
    Le symbole ⬅️ indique la réponse sortante.
    On renvoie ensuite la réponse au client.


Le middleware utilise la classe `BaseHTTPMiddleware` de Starlette et le logger configuré dans `app/core/logging_config.py`.
Il renforce l’observabilité et la transparence du fonctionnement de l’API.
"""

from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logging_config import get_logger

logger = get_logger()

class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger.info(f"➡️ {request.method} {request.url}")
        response = await call_next(request)
        logger.info(f"⬅️ {response.status_code} {request.url}")
        return response
