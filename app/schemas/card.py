from datetime import date
from typing import Optional

from sqlmodel import Field, SQLModel


class CardBase(SQLModel):
    number: str
    holder: str
    expiration: date = Field(default=date.today())
    cvv: str
    credit_limit: float = 0.0


class CardCreate(CardBase):
    """Schema for creating a new credit card."""

    account_id: Optional[int] = Field(
        default=None, description="Associated bank account ID"
    )


class CardRead(CardBase):
    id: int
    credit_limit: float = 0.0
    is_active: bool = True


class CardUpdate(SQLModel):
    holder: Optional[str] = Field(default=None)
    credit_limit: Optional[float] = Field(default=None)
    expiration: Optional[date] = Field(default=None)
    cvv: Optional[str] = Field(default=None)
