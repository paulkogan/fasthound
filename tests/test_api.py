import pytest
from starlette.status import HTTP_200_OK
from starlette.testclient import TestClient

from app import app

from .conftest import Factory

pytestmark = pytest.mark.usefixtures("inject_session")


def test_list_energizers(api_client: TestClient, make_energizer: Factory[dict]) -> None:
    url = app.url_path_for("list_energizers")
    response = api_client.get(url)

    assert response.status_code == HTTP_200_OK
    response_energizers = response.json()
    assert len(response_energizers) == 6
