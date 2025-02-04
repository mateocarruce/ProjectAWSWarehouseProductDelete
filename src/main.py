from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Product Deletion Microservice")

app.include_router(router)
