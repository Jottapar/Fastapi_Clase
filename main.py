from fastapi import FastAPI
from app.api.usuario_router import router as user_router
from app.api.auth_router import router as login_router
from app.api.acta_router import router as acta_router
from app.api.orden_trabajo_router import router as orden_trabajo_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(user_router)
app.include_router(login_router)
app.include_router(acta_router)
app.include_router(orden_trabajo_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi primera API con FASTAPI!"}

