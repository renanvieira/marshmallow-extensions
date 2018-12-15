# Marshmallow Schema Fields Extension
Extension fields to use along with [Marshmallow](https://marshmallow.readthedocs.io/en/2.x-line/) schemas.



## Custom Fields

### EnumField
Field to validate if the input string is a enum value.

```python
from enum import Enum
from marshmallow import Schema

class FrequencyEnum(Enum):
    Daily = 'daily'
    Monthly = 'monthly'
    Weekly = 'weekly'
    Annually = 'annually'


class CustomSchema(Schema):
    frequency = EnumField(enum=FrequencyEnum, required=True)
```

### PositiveInteger

Validates if the integer is positive, you can use the param `allow_zero` to set if zero is a valid value.

On this exemple, any number lesser than or equal to zero will throw an error during validation.
```python
from marshmallow import Schema

class CustomSchema(Schema):
    amount = PositiveInteger(required=False)    

```
To allow zero, just pass the param `allow_zero=True` during field initialization.
```python
from marshmallow import Schema

class CustomSchema(Schema):
    amount = PositiveInteger(allow_zero=True, required=False)    

```

### Hex UUID

Validates if it is a UUID valid and return the [hex value](https://docs.python.org/3.6/library/uuid.html#uuid.UUID.hex), instead of pythons native UUID instance when it's valid.

```python
from marshmallow import Schema

class CustomSchema(Schema):
    id = UUIDHex(required=False)    

```