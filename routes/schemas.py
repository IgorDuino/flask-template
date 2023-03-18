from pydantic import BaseModel
from uuid import UUID
from enum import Enum


class EnumType(str, Enum):
    enum1 = "enum1"
    enum2 = "enum2"


class UnitType(BaseModel):
    name: str
    text: str
    some_enum: EnumType

    class Config:
        use_enum_values = True


class UserImport(BaseModel):
    username: str
    email: str
    password: str
