from fastapi import FastAPI

from backend.src.core.settings import settings
from backend.src.api.routers.users import (router as users)


app = FastAPI()
app.include_router(users)


@app.get(settings.main_url)
async def root():
    return {"message": "200"}
