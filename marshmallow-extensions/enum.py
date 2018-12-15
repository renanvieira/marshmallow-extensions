from marshmallow import fields
from marshmallow.utils import missing as missing_


class EnumField(fields.Field):
    default_error_messages = {
        'invalid_enum': 'Value provided is not valid.',
    }

    def __init__(self, enum, required=False, load_only=False, default=missing_, missing=missing_, dump_only=False,
                 attribute=None, load_from=None, dump_to=None, error=None, validate=None, allow_none=None,
                 error_messages=None, **metadata):

        self.enum_type = enum
        super().__init__(default, attribute, load_from, dump_to, error, validate, required, allow_none, load_only,
                         dump_only, missing, error_messages, **metadata)

    def _validated(self, value):
        """Format the value or raise a :exc:`ValidationError` if an error occurs."""
        try:
            if value is None:
                return None

            if self.enum_type.has_value(value) is False:
                raise ValueError("value not defined in enum.")

            return self.enum_type(value)

        except (TypeError, ValueError):
            self.fail('invalid_enum')

    def _deserialize(self, value, attr, data):
        try:
            if isinstance(value, self.enum_type):
                return value.value
            else:
                return self._validated(value).value

        except Exception as e:
            self.fail("invalid_enum")

    def _serialize(self, value, attr, obj):

        try:
            if isinstance(value, self.enum_type):
                return value.value
            else:
                return self._validated(value).value

        except Exception as e:
            self.fail("invalid_enum")
