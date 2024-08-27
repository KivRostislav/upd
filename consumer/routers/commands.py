from traceback import print_tb

from fastapi import APIRouter
from starlette.websockets import WebSocket

from logger import LOGGER
from models.command import ExecuteCommandRequest
from repositories import command_repository

router: APIRouter = APIRouter(prefix="/commands", tags=["commands"])

class Execute:
    def comm(self):
        print("From pass")

@router.websocket("/ws")
async def connect(websocket: WebSocket):
    LOGGER.info("Staertr")
    socket = await websocket.accept()
    while True:
        message = (await websocket.receive()).get('text')
        LOGGER.info(message)
        request = ExecuteCommandRequest.model_validate_json(message)
        commands = list(filter(lambda x : x.id == request.command_id, command_repository.commands()))
        if len(commands) <= 0:
            await websocket.send_text("Command not found")

        exec(open(commands[0].script, 'r').read(), {'none': Execute()})


