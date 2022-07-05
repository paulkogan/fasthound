from typing import Callable, ContextManager, List, Any, Union
from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK
from config import cfg
from core import energizers

from database import ENGINE, session_maker
from models import EngSelect
from core.schemas import EnergizerOut

router = APIRouter()


def session_maker_factory() -> Callable[[], ContextManager[Session]]:
    return lambda: session_maker(bind=ENGINE)


@router.get("/hello")
async def hello_response():
    return {"message": f"Hello API Fasthound 4 {cfg.DB_HOST}"}


@router.get("/parameters/{path_param}")
def show_parameters(
    multi: Union[int, None] = None,
    path_param: str = None,
    snake_header: Union[str, None] = Header(default=None),
) -> List[Any]:

    results = f"RETURNING: path_param: {path_param}"
    if multi:
        results += f" and query_multi = {11*multi}"

    if snake_header:
        results += f" and snake_header param = {snake_header}"

    return results


@router.get(
    "/energizers/{energizer_id}", response_model=EnergizerOut, status_code=HTTP_200_OK
)  # noqa: E501
async def retrieve_energizer(
    energizer_id: int,
    session_maker_instance: Callable[[], ContextManager[Session]] = Depends(
        session_maker_factory
    ),
) -> EnergizerOut:
    raw_energizer = energizers.retrieve_energizer(
        energizer_id, session_factory=session_maker_instance
    )
    if not raw_energizer:
        raise HTTPException(
            status_code=404, detail=f"Energizer id: {energizer_id} not found"
        )

    return raw_energizer


@router.get("/energizers", response_model=List[EnergizerOut], status_code=HTTP_200_OK)
def list_energizers(
    session_maker_instance: Callable[[], ContextManager[Session]] = Depends(
        session_maker_factory
    )
) -> List[EngSelect]:
    raw_energizers = energizers.list_energizers(session_factory=session_maker_instance)

    return raw_energizers
