from typing import Callable, ContextManager, List, Any, Union
from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK
from config import cfg
from core import energizers

from database import ENGINE, session_maker
from models import EngSelect
from core.schemas import EnergizerResponse, EnergizerRequest

router = APIRouter()


def get_db() -> Callable[[], ContextManager[Session]]:
    return lambda: session_maker(bind=ENGINE)


@router.post("/energizers")
def create_energizer(
    payload: EnergizerRequest,
    session_maker_instance: Callable[[], ContextManager[Session]] = Depends(get_db),
) -> EnergizerRequest:
    new_energizer = energizers.create_energizer(
        payload, session_factory=session_maker_instance
    )

    return new_energizer


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
    "/energizers/{energizer_id}",
    response_model=EnergizerResponse,
    status_code=HTTP_200_OK,
)  # noqa: E501
async def retrieve_energizer(
    energizer_id: int,
    session_maker_instance: Callable[[], ContextManager[Session]] = Depends(get_db),
) -> EnergizerResponse:
    raw_energizer = energizers.retrieve_energizer(
        energizer_id, session_factory=session_maker_instance
    )
    if not raw_energizer:
        raise HTTPException(
            status_code=404, detail=f"Energizer id: {energizer_id} not found"
        )

    return raw_energizer


@router.get(
    "/energizers", response_model=List[EnergizerResponse], status_code=HTTP_200_OK
)
def list_energizers(
    session_maker_instance: Callable[[], ContextManager[Session]] = Depends(get_db)
) -> List[EngSelect]:
    raw_energizers = energizers.list_energizers(session_factory=session_maker_instance)

    return raw_energizers


@router.get("/hello")
async def hello_response():
    return {"message": f"Hello API Fasthound 4 {cfg.DB_HOST}"}
