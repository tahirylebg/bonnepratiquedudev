from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles

from app.api import books, orders
from app.middlewares.request_logger import RequestLoggerMiddleware
from app.middlewares.error_handler import setup_error_handlers


# --- Création de l'application principale ---
app = FastAPI(
    title="📚 Bookstore API",
    description="""
Bienvenue sur **Bookstore API**, une application de gestion de livres moderne et élégante 💡

Fonctionnalités principales :
- 📗 **Lister** les livres disponibles  
- ➕ **Ajouter** de nouveaux ouvrages  
- 🛒 **Créer des commandes**  
- 📖 **Rechercher book**
- ⚙️ **Suivre les logs et erreurs** en temps réel  

> Développé avec **FastAPI**, respectant les bonnes pratiques de développement et de documentation.
    """,
    version="1.0.0",
    contact={
        "name": "Bookstore Team",
        "email": "contact@bookstore.dev",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    docs_url=None,  # on va redéfinir une page Swagger custom plus bas
)

# --- Fichiers statiques (CSS, favicon, logo) ---
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# --- Page Swagger customisée ---
@app.get("/docs", include_in_schema=False)
async def custom_docs():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="📘 Bookstore API — Interface Moderne",
        swagger_favicon_url="/static/favicon.ico",  # favicon perso (à mettre dans app/static)
        swagger_css_url="/static/custom_swagger.css",  # ton fichier CSS
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1,
            "displayRequestDuration": True,
            "docExpansion": "list",
            "filter": True,
        },
    )


# --- Endpoint pour exposer la spec OpenAPI ---
@app.get("/openapi.json", include_in_schema=False)
async def custom_openapi():
    return get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )


# --- Endpoint d'accueil ---
@app.get("/")
def home():
    return {"message": "Bienvenue dans la boutique de livres 📚"}


# --- Routes principales ---
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

# --- Middlewares ---
app.add_middleware(RequestLoggerMiddleware)
setup_error_handlers(app)
