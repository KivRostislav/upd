import os
from os import path
from typing import List

from pydantic import TypeAdapter

from models.command import Command

COMMANDS: List[Command] = []
DEFAULT_COMMANDS_STORE_FILE_PATH: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")


def initialize(path_to_config: str) -> None:
    if not path.isfile(path_to_config):
        raise FileNotFoundError

    global COMMANDS
    adapter = TypeAdapter(List[Command])
    with open(path_to_config, 'r') as instance:
        COMMANDS = adapter.validate_json(instance.read())

def commands() -> List[Command]:
    return COMMANDS
