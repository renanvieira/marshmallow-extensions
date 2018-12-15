import uuid

from marshmallow.fields import UUID


class UUIDHex(UUID):
    """A UUID field which returns hex."""

    def _validated(self, value):
        """Format the value or raise a :exc:`ValidationError` if an error occurs."""
        if value is None:
            return None
        if isinstance(value, uuid.UUID):
            return value.hex
        try:
            return uuid.UUID(value).hex
        except (ValueError, AttributeError):
            self.fail('invalid_uuid')
