from typing import Callable, ContextManager, Union
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models import EngSelect, EngCreateInitial
from core.schemas import EnergizerIn


def create_energizer(
    payload: EnergizerIn, session_factory: Callable[[], ContextManager[Session]]
) -> EnergizerIn:
    payload.wiki_page = (
        "https://en.wikipedia.org/wiki/" + payload.first_name + "_" + payload.last_name
    )
    energizer_submit = EngCreateInitial(
        first_name=payload.first_name,
        last_name=payload.last_name,
        occupation=payload.occupation,
        wiki_page=payload.wiki_page,
    )

    with session_factory() as session:
        session.add(energizer_submit)
        session.commit()

    return payload


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
