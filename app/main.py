from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI

from app.api import books, orders
from app.middlewares.request_logger import RequestLoggerMiddleware
from app.middlewares.error_handler import setup_error_handlers

app = FastAPI(
    title="📚 Bookstore API",
    description="API de gestion d'une boutique de livres moderne et élégante 💡",
    version="1.0.0",
    contact={
        "name": "Bookstore Team",
        "email": "contact@bookstore.dev"
    },
    docs_url=None
)

@app.get("/docs", include_in_schema=False)
async def custom_docs():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="📘 Bookstore API — Interface Moderne",
        swagger_favicon_url="https://cdn-icons-png.flaticon.com/512/29/29302.png",
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1,
            "displayRequestDuration": True,
            "docExpansion": "list",
            "filter": True,
        },
    )

@app.get("/openapi.json", include_in_schema=False)
async def custom_openapi():
    return get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

@app.get("/")
def home():
    return {"message": "Bienvenue dans la boutique de livres 📚"}

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

app.add_middleware(RequestLoggerMiddleware)
setup_error_handlers(app)
