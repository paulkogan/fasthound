import pytest
from freezegun import freeze_time
from starlette.status import HTTP_200_OK
from starlette.testclient import TestClient

from app import app
from core.test_messages.serializers import TestMessageRequest

from .conftest import Factory

pytestmark = pytest.mark.usefixtures("inject_session")


@freeze_time()
def test_udpate_test_message_updates_message(
    api_client: TestClient,
    test_message_request_update: TestMessageRequest,
    make_test_message: Factory[dict],
) -> None:
    orig_test_message = make_test_message()

    url = app.url_path_for("update_test_message", message_id=orig_test_message["id"])

    response = api_client.patch(
        url,
        json=test_message_request_update.dict(),
    )
    assert response.status_code == HTTP_200_OK, response.json()
    response_payload = response.json()
    id_ = response_payload["id"]
    date_ = response_payload["created"]
    assert response_payload == {
        "id": id_,
        "created": date_,
        **test_message_request_update.dict(),
    }
