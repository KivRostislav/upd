from typing import List

from models.session import Session

SESSIONS: List[Session] = []

def sessions() -> List[Session]:
    return SESSIONS