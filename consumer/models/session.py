from typing import List

from pydantic import BaseModel


class Session(BaseModel):
    id: int
    executed_commands: List[int]