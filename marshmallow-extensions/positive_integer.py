from marshmallow.fields import Number


class PositiveInteger(Number):
    """Base class for positive integer fields.

    :param bool as_string: If True, format the serialized value as a string.
    :param kwargs: The same keyword arguments that :class:`Field` receives.
    """

    num_type = int
    default_error_messages = {
        'invalid': 'Not a valid integer. Check if is a valid, greater than or equal to zero, integer.',
        'invalid_zero': 'Not a valid integer. Check if is a valid, greater than zero, integer.'
    }

    def __init__(self, as_string=False, allow_zero=False, **kwargs):
        self.as_string = as_string
        self.allow_zero = allow_zero
        super(Number, self).__init__(**kwargs)

    def _validated(self, value):
        """Format the value or raise a :exc:`ValidationError` if an error occurs."""
        message = "invalid_zero"
        try:
            validated_integer = self._format_num(value)

            if self.allow_zero is True:
                message = "invalid"
                if validated_integer < 0:
                    raise ValueError("Negative integer not allowed")
            else:
                if validated_integer <= 0:
                    raise ValueError("Negative and Zero integer not allowed")

            return validated_integer
        except (TypeError, ValueError):
            self.fail(message)
