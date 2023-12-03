
from typing import (
    Any,
    Generic,
    Tuple,
    Type,
    TypeVar,
    Union,
)

VALUE = TypeVar("VALUE")

class _FieldMeta(type):
    # TODO: Require functions to return field instances instead of this hack
    def __new__(mcs, name: str, bases: Tuple[Type, ...], attrs: dict):
        if len(bases) > 1 and bases[0] is Field:
            # Instantiate class with only the 1st base class (should be Field)
            cls = type.__new__(mcs, name, (bases[0],), attrs)
            # All other base classes are our meta types, we store them in class attributes
            cls.field_type = bases[1] if len(bases) == 2 else Union[bases[1:]]  # type: ignore
            return cls
        return type.__new__(mcs, name, bases, attrs)

class Field(Generic[VALUE], metaclass=_FieldMeta):
    def __init__(
            self,
            default: Any=None,
            description:str = None

    )->None:
        print("Field.__init__ called")
        self.default = default
        self.description = description


class CharField(Field):
    def __init__(
        self,
        max_length: int = 255,
        *args,
        **kwargs,
    ) -> None:
        print("CharField.__init__ called")
        self.max_length = max_length
        super().__init__(*args, **kwargs)

class IntField(Field):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        pass

class DateField(Field):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        pass
class FloatField(Field):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        pass

    
