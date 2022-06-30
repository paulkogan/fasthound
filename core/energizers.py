from datetime import datetime
from typing import Callable, ContextManager, Any
from uuid import UUID, uuid4

import pytz
from sqlalchemy import select, update
from sqlalchemy.orm import Session

# from core.test_messages.serializers import TestMessageRequest
# from models import TestMessage


# def create_test_message(
#     payload: TestMessageRequest, session_factory: Callable[[], ContextManager[Session]]
# ) -> TestMessage:
#     test_message = TestMessage(
#         id=uuid4(),
#         prescriber_id=payload.prescriber_id,
#         drug_id=payload.drug_id,
#         status=payload.status,
#         prescriber_order_number=payload.prescriber_order_number,
#         created=datetime.now(tz=pytz.UTC),
#     )

#     with session_factory() as session:
#         session.add(test_message)
#         session.commit()

#     return test_message


def list_energizers(
    session_factory: Callable[[], ContextManager[Session]]
) -> list[Any]:
    with session_factory() as session:
        return list(session.execute(select(Any)).scalars())


# def get_test_message(message_id: UUID, session_factory: Callable[[], ContextManager[Session]]) -> TestMessage:
#     with session_factory() as session:
#         return session.execute(select(TestMessage).where(TestMessage.id == message_id)).scalar_one()


# def update_test_message(
#     message_id: UUID, payload: TestMessageRequest, session_factory: Callable[[], ContextManager[Session]]
# ) -> TestMessage:
#     with session_factory() as session:
#         stmt = (
#             update(TestMessage)
#             .where(TestMessage.id == message_id)
#             .values(
#                 prescriber_id=payload.prescriber_id,
#                 drug_id=payload.drug_id,
#                 status=payload.status,
#                 prescriber_order_number=payload.prescriber_order_number,
#             )
#             .returning(TestMessage)
#         )
#         orm_stmt = select(TestMessage).from_statement(stmt).execution_options(populate_existing=True)
#         test_message = session.execute(orm_stmt).scalar_one()
#         session.commit()
#         return test_message
