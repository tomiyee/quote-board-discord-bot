import uuid
from typing import NewType

from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.decl_api import _TypeAnnotationMapType

SpeakerID = NewType("SpeakerID", uuid.UUID)
QuoteID = NewType("QuoteID", uuid.UUID)

CUSTOM_UUID_TYPES = [SpeakerID, QuoteID]


class Base(DeclarativeBase):
    type_annotation_map: _TypeAnnotationMapType = {
        # Define mapping of Python UUID types to SQLAlchemy UUID type
        uuid.UUID: UUID(as_uuid=True),
        **{uuid_type: UUID(as_uuid=True) for uuid_type in CUSTOM_UUID_TYPES},
    }
