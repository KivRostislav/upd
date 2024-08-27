from fastapi import FastAPI

from routers.commands import router as commands_router

def configure_routes(app: FastAPI) -> None:
    app.include_router(commands_router)
