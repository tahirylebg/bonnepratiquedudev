"""
error_handler.py : Gestion centralisée des erreurs FastAPI.

Ce module définit des *handlers* (gestionnaires) pour intercepter et traiter toutes les erreurs de l’application :
    -`HTTPException` c'est les erreurs connues avec message clair pour le client.
    -`Exception` c'est les erreurs inattendues (bug, crash...) renvoyant un message générique.

Comment ca fonctionne :
 -Quand une erreur survient dans une route, FastAPI redirige automatiquement vers le handler approprié.
 -Le handler enregistre l’erreur dans les logs (loguru)
 -Le client reçoit une réponse JSON propre et lisible (pas une trace Python).
 Dans le premier gestionnaire :
    Quand une erreur HTTP (comme 404, 400, 403…) est levée dans l’application,
    on intercepte l’erreur, on l’écrit dans les logs (niveau WARNING),
    et on renvoie une réponse JSON avec le message d’erreur et le code correspondant
 Dans le second :
    Si une erreur non prévue survient, on la capture pour éviter que l’application plante,
    on la log (niveau ERROR), et on renvoie une réponse JSON générique
    indiquant une erreur serveur (code 500) .


"""

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from loguru import logger

def setup_error_handlers(app):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.warning(f"HTTP Error {exc.status_code}: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled error: {exc}")
        return JSONResponse(status_code=500, content={"error": "Erreur interne du serveur"})
