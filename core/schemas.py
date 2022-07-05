from typing import Union
from pydantic import BaseModel


class Non200Response(BaseModel):
    error: str


class EnergizerOut(BaseModel):
    id: int
    first_name: str
    last_name: Union[str, None]
    wiki_page: Union[str, None]
    born_state: Union[str, None]
    born_town: Union[str, None]

    class Config:
        orm_mode = True
