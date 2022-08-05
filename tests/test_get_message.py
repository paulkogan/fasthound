import pytest
from starlette.status import HTTP_200_OK
from starlette.testclient import TestClient

from .conftest import Factory

pytestmark = pytest.mark.usefixtures("inject_session")


def test_get_message_details(
    api_client: TestClient, make_test_message: Factory[dict]
) -> None:
    test_message = make_test_message()

    response = api_client.get(
        f"/svc/non-ro-pharmacies/any/messages/{test_message['id']}"
    )

    assert response.status_code == HTTP_200_OK, response.json()
