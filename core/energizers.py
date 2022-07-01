from datetime import datetime
from typing import Callable, ContextManager, Any
from uuid import UUID, uuid4

import pytz
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from models import Energizer


def list_energizers(
    session_factory: Callable[[], ContextManager[Session]]
) -> list[Energizer]:
    with session_factory() as session:
        return list(session.execute(select(Energizer)).scalars())
