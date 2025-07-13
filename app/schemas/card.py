from datetime import date
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class CreditCard(BaseModel):
    card_id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique identifier for the credit card",
    )
    card_number: str = Field(default="", description="Credit card number")
    cardholder_name: str = Field(default="", description="Name of the cardholder")
    expiration_date: date = Field(
        default_factory=date.today, description="Expiration date of the card"
    )
    cvv: str = Field(default="", description="Card Verification Value")
    credit_limit: float = Field(default=0.0, description="Maximum credit limit")
    is_active: bool = Field(default=True, description="Indicates if the card is active")
    account_id: Optional[str] = Field(
        default=None, description="Associated account identifier"
    )
