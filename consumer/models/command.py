from pydantic import BaseModel


class Command(BaseModel):
    id: int
    name: str
    script: str

class ExecuteCommandRequest(BaseModel):
    command_id: int
    session_id: int
