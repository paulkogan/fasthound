from typing import Callable, ContextManager, Generator, TypeVar

import pytest
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session

from starlette.testclient import TestClient

# from fastapi.testclient import TestClient

from api.api import get_db
from app import app
from core.schemas import EnergizerRequest
from database import ENGINE, session_maker

T = TypeVar("T")

YieldFixture = Generator[T, None, None]
Factory = Callable[[], T]


@pytest.fixture
def api_client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def connection() -> YieldFixture[Connection]:
    with ENGINE.connect() as connection:
        with connection.begin() as transaction:
            yield connection

            transaction.rollback()


@pytest.fixture
def session_factory(connection: Connection) -> Factory[ContextManager[Session]]:
    return lambda: session_maker(bind=connection)


@pytest.fixture
def session(session_factory: Factory[ContextManager[Session]]) -> YieldFixture[Session]:
    with session_factory() as session:
        yield session


@pytest.fixture
def energizer_request() -> EnergizerRequest:
    return EnergizerRequest(
        first_name="Newell",
        last_name="Gollum",
        occupation="lion",
    )


@pytest.fixture
def inject_session(session_factory: Factory[ContextManager[Session]]):
    app.dependency_overrides[get_db] = lambda: session_factory

    yield session_factory

    app.dependency_overrides = {}


@pytest.fixture
def make_energizer(
    api_client: TestClient, energizer_request: EnergizerRequest
) -> Factory[dict]:
    def factory() -> dict:
        response = api_client.post(
            app.url_path_for("create_energizer"), json=energizer_request.dict()
        )

        return response.json()

    return factory
