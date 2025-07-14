from datetime import date
from typing import Optional

from sqlmodel import Field, SQLModel


class CardBase(SQLModel):
    number: str
    holder: str
    expiration: str = Field(default=date.today().isoformat())
    cvv: str
    credit_limit: float = 0.0


class CardCreate(CardBase):
    pass


class CardRead(CardBase):
    id: int
    credit_limit: float = 0.0
    is_active: bool = True


class CardUpdate(SQLModel):
    holder: Optional[str] = Field(default=date.today().isoformat())
    credit_limit: Optional[float] = Field(default=None)
    expiration: Optional[str] = Field(default=None)
    cvv: Optional[str] = Field(default=None)
