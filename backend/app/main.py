from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.core.config import settings
from app.db.indexes import ensure_indexes
from app.db.mongo import close_client
from app.seed.seed_data import seed
from app.routers import auth, users, categories, products, bookings, payments, dashboard

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS if settings.CORS_ORIGINS != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(bookings.router)
app.include_router(payments.router)
app.include_router(dashboard.router)


@app.on_event("startup")
async def startup():
    await ensure_indexes()
    await seed()


@app.on_event("shutdown")
async def shutdown():
    await close_client()


@app.get("/api/health")
async def health():
    return {"ok": True, "service": settings.PROJECT_NAME, "db": settings.DB_NAME, "env_source": settings.COLLAB_ENV_PATH}


# Serve frontend in dev if present
FRONTEND_DIR = Path(__file__).resolve().parents[2] / "frontend"
if FRONTEND_DIR.exists():
    assets = FRONTEND_DIR / "assets"
    if assets.exists():
        app.mount("/assets", StaticFiles(directory=str(assets)), name="assets")

    @app.get("/")
    async def root():
        index = FRONTEND_DIR / "index.html"
        if index.exists():
            return FileResponse(str(index))
        return {"ok": True}

    @app.get("/{page}.html")
    async def html_page(page: str):
        f = FRONTEND_DIR / f"{page}.html"
        if f.exists():
            return FileResponse(str(f))
        return FileResponse(str(FRONTEND_DIR / "index.html")) if (FRONTEND_DIR / "index.html").exists() else {"detail": "Not found"}
