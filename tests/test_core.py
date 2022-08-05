from datetime import datetime
from typing import ContextManager, Protocol

import pytz
from freezegun import freeze_time
from sqlalchemy import select
from sqlalchemy.orm import Mapper, Session

from core.test_messages.serializers import TestMessageRequest
from core.test_messages.test_messages import create_test_message
from models import TestMessage

from .conftest import Factory


class SQLAlchemyModel(Protocol):
    __mapper__: Mapper


def get_names(entity: SQLAlchemyModel) -> set[str]:
    """Get names of fields from sqlalchemy model."""
    return set(entity.__mapper__.attrs.keys())


def assert_models_equal(left: SQLAlchemyModel, right: SQLAlchemyModel) -> None:
    """Assert equality on sqlalchemy models, which are normally compared by identity."""
    left_fields = get_names(entity=left)
    right_fields = get_names(entity=right)

    if left_diff := left_fields - right_fields:
        assert (
            not left_diff
        ), f"Fields in the left model, but not right: {', '.join(left_diff)}."

    if right_diff := right_fields - left_fields:
        assert (
            not right_diff
        ), f"Fields in the right model, but not left: {', '.join(right_diff)}."

    for name in left_fields:
        left_value = getattr(left, name)
        right_value = getattr(right, name)

        assert (
            left_value == right_value
        ), f"Difference at field {name}, {left_value} != {right_value}."


@freeze_time()
def test_create_persists_test_message(
    session_factory: Factory[ContextManager[Session]],
    test_message_request: TestMessageRequest,
) -> None:
    test_message = create_test_message(
        payload=test_message_request, session_factory=session_factory
    )

    with session_factory() as session:
        test_message_from_db = session.execute(select(TestMessage)).scalars().one()

        assert_models_equal(test_message_from_db, test_message)

    assert test_message.prescriber_id == test_message_request.prescriber_id
    assert test_message.drug_id == test_message_request.drug_id
    assert test_message.status == test_message_request.status
    assert (
        test_message.prescriber_order_number
        == test_message_request.prescriber_order_number
    )
    assert test_message.created == datetime.now(tz=pytz.UTC)
