from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="The multilingual African AI platform.",
    version=settings.VERSION,
)

app.include_router(
    api_router,
    prefix=settings.API_PREFIX,
)


@app.get("/")
def root():
    return {
        "message": "Murakaza neza kuri Bwenge!",
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "running",
    }