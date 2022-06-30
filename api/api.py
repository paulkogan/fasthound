from typing import Callable, ContextManager
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from core import energizers

# from core.test_messages.serializers import TestMessageRequest, TestMessageResponse, TestMessagesList
from database import ENGINE, session_maker

router = APIRouter()


@router.get("/hello")
async def hello_response():
    return {"message": "Hello from Non-Ro-Pharmacies"}


def session_maker_factory() -> Callable[[], ContextManager[Session]]:
    return lambda: session_maker(bind=ENGINE)


@router.get("/messages/{message_id}", status_code=HTTP_200_OK)
def get_message_details(
    message_id: UUID,
    session_maker: Callable[[], ContextManager[Session]] = Depends(
        session_maker_factory
    ),
) -> TestMessageResponse:
    test_message = test_messages_core.get_test_message(
        message_id=message_id, session_factory=session_maker
    )

    return TestMessageResponse.from_model(test_message)


@router.post("/messages", status_code=HTTP_201_CREATED)
def create_test_message(
    payload: TestMessageRequest,
    session_maker: Callable[[], ContextManager[Session]] = Depends(
        session_maker_factory
    ),
) -> TestMessageResponse:
    test_message = test_messages_core.create_test_message(
        payload=payload, session_factory=session_maker
    )

    return TestMessageResponse.from_model(test_message)


@router.get("/messages", status_code=HTTP_200_OK)
def list_test_messages(
    session_maker: Callable[[], ContextManager[Session]] = Depends(
        session_maker_factory
    )
) -> TestMessagesList:
    test_messages = test_messages_core.list_test_messages(session_factory=session_maker)

    return TestMessagesList(
        data=[
            TestMessageResponse.from_model(test_message)
            for test_message in test_messages
        ]
    )


@router.patch("/messages/update/{message_id}", status_code=HTTP_200_OK)
def update_test_message(
    message_id: UUID,
    payload: TestMessageRequest,
    session_maker: Callable[[], ContextManager[Session]] = Depends(
        session_maker_factory
    ),
) -> TestMessageResponse:
    test_message = test_messages_core.update_test_message(
        message_id=message_id, payload=payload, session_factory=session_maker
    )

    return TestMessageResponse.from_model(test_message)


@router.post("/prescriptions", status_code=HTTP_201_CREATED)
def create_prescription(
    prescription_payload: CreatePrescriptionRequest,
) -> CreatePrescriptionResponse:
    newrx_response = gateway_core.create_dummy_newrx(payload=prescription_payload)

    return newrx_response


@router.post("/prescriptions/mock", status_code=HTTP_201_CREATED)
def create_prescription_mock(
    prescription_payload: CreatePrescriptionRequest,
) -> CreatePrescriptionResponse:
    newrx_response = gateway_core.send_newrx(
        source_json=jsonable_encoder(prescription_payload),
        ro_plan_uuid=prescription_payload.medication.ro_plan_uuid,
    )

    return newrx_response
