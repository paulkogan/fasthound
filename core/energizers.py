from typing import Callable, ContextManager, Union
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models import EngSelect


def list_energizers(
    session_factory: Callable[[], ContextManager[Session]]
) -> list[EngSelect]:
    with session_factory() as session:
        return list(session.execute(select(EngSelect)).scalars())


def retrieve_energizer(
    energizer_id: int, session_factory: Callable[[], ContextManager[Session]]
) -> Union[EngSelect, None]:
    with session_factory() as session:
        try:
            results = session.execute(
                select(EngSelect).where(EngSelect.id == energizer_id)
            ).scalar_one()
        except NoResultFound:
            print("No Result Found Error")
            results = None

        return results
