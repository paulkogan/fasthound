import pytest
from starlette.status import HTTP_200_OK
from starlette.testclient import TestClient

from app import app

from .conftest import Factory

pytestmark = pytest.mark.usefixtures("inject_session")


def test_list_messages_returns_all_messages(
    api_client: TestClient, make_test_message: Factory[dict]
) -> None:
    url = app.url_path_for("list_test_messages")
    test_messages = [make_test_message() for _ in range(3)]

    response = api_client.get(url)

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"data": test_messages}
