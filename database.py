from contextlib import contextmanager
from typing import Generator, Union

from sqlalchemy import create_engine
from sqlalchemy.engine import Connection, Engine, make_url
from sqlalchemy.orm import Session  # sessionmaker

from config import cfg

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
URL = make_url(
    f"postgresql://{cfg.DB_USER}:{cfg.DB_PASSWORD}@{cfg.DB_HOST}:{cfg.DB_PORT}/{cfg.DB_DATABASE}"
)

ENGINE = create_engine(URL)


@contextmanager
def session_maker(bind: Union[Connection, Engine]) -> Generator[Session, None, None]:
    with Session(bind=bind, expire_on_commit=False) as session:
        yield session
