import os
from contextlib import asynccontextmanager
from logger import LOGGER
from fastapi import FastAPI

from parameters import EnvKeys
from repositories.command_repository import DEFAULT_COMMANDS_STORE_FILE_PATH, initialize


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    on_startup(app)
    yield
    on_shutdown(app)

def on_startup(_: FastAPI) -> None:
    LOGGER.info("Startup")

    commands_store_file: str | None = os.environ.get(EnvKeys.COMMANDS_STORE_FILE)
    if commands_store_file is None:
        commands_store_file = DEFAULT_COMMANDS_STORE_FILE_PATH

    initialize(commands_store_file)


def on_shutdown(_: FastAPI) -> None:
    LOGGER.info("Shutdown")