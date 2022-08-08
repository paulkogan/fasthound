from typing import Union
from pydantic import BaseModel


class Non200Response(BaseModel):
    error: str


class EnergizerRequest(BaseModel):
    first_name: str
    last_name: str
    occupation: str
    wiki_page: Union[str, None] = None

    class Config:
        orm_mode = True


class EnergizerResponse(BaseModel):
    id: int
    first_name: Union[str, None]
    last_name: Union[str, None]
    wiki_page: Union[str, None]
    born_state: Union[str, None]
    born_town: Union[str, None]
    occupation: Union[str, None]
    
    class Config:
        orm_mode = True
