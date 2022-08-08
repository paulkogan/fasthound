import pytest
from starlette.status import HTTP_200_OK, HTTP_201_CREATED
from core.schemas import EnergizerRequest

from app import app

# use inject session to roll back transactions after test
pytestmark = pytest.mark.usefixtures("inject_session")

def test_list_energizers(api_client, make_energizer) -> None:
    url = app.url_path_for("list_energizers")
    response = api_client.get(url)

    assert response.status_code == HTTP_200_OK
    response_energizers = response.json()
    assert len(response_energizers) > 0


def test_get_energizer_details(api_client, make_energizer) -> None:
    lion_energizer = make_energizer()
    target_id = lion_energizer["id"]
    response = api_client.get(f"/energizers/{target_id}")

    assert response.status_code == HTTP_200_OK, response.json()
    energizer_details = response.json()
    print(energizer_details)
    assert energizer_details["id"] == target_id
    assert energizer_details["occupation"] == "lion"


def test_post_new_energizer(
    api_client, energizer_request: EnergizerRequest
) -> None:
    url = app.url_path_for("create_energizer")

    response = api_client.post(
        url,
        json=energizer_request.dict(),
    )

    assert response.status_code == HTTP_200_OK, response.json()
    response_payload = response.json()
    assert response_payload["id"]
    assert response_payload["occupation"] == "lion"
