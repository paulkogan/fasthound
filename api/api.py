from typing import Callable, ContextManager, List, Any
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED
from config import cfg
from core import energizers

from database import ENGINE, session_maker

router = APIRouter()


def session_maker_factory() -> Callable[[], ContextManager[Session]]:
    return lambda: session_maker(bind=ENGINE)


@router.get("/hello")
async def hello_response():
    return {"message": f"Hello API Fasthound 4 {cfg.DB_HOST}"}


@router.get("/energizers", status_code=HTTP_200_OK)
def list_energizers(
    session_maker: Callable[[], ContextManager[Session]] = Depends(
        session_maker_factory
    )
) -> List[Any]:
    raw_energizers = energizers.list_energizers(session_factory=session_maker)

    return raw_energizers
