from datetime import datetime

import pytest
import pytz
from freezegun import freeze_time
from starlette.status import HTTP_201_CREATED
from starlette.testclient import TestClient

from app import app
from core.test_messages.serializers import TestMessageRequest

pytestmark = pytest.mark.usefixtures("inject_session")


@freeze_time()
def test_post_test_message_creates_new_message(
    api_client: TestClient, test_message_request: TestMessageRequest
) -> None:
    url = app.url_path_for("create_test_message")

    response = api_client.post(
        url,
        json=test_message_request.dict(),
    )

    assert response.status_code == HTTP_201_CREATED, response.json()
    response_payload = response.json()
    id_ = response_payload["id"]
    assert response_payload == {
        "id": id_,
        "created": datetime.now(tz=pytz.UTC).isoformat(),
        **test_message_request.dict(),
    }
