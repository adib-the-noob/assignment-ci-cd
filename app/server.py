from fastapi import FastAPI
from app.router.smoke_test import router as smoke_router
app = FastAPI()

app.include_router(smoke_router)