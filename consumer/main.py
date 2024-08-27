from fastapi import FastAPI

from lifespan import lifespan
from router import configure_routes

app = FastAPI(lifespan=lifespan)
configure_routes(app)