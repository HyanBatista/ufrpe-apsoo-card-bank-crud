from datetime import datetime, timezone
from decimal import Decimal
from uuid import uuid4

from pydantic import BaseModel, Field


class BankAccount(BaseModel):
    account_id: str = Field(default_factory=lambda: str(uuid4()))
    owner_name: str = Field(
        ..., title="Owner Name", description="Full name of the account owner"
    )
    balance: Decimal = Field(
        default=Decimal("0.00"), title="Balance", description="Current account balance"
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        title="Created At",
        description="Account creation timestamp",
    )
    is_active: bool = Field(
        default=True,
        title="Is Active",
        description="Indicates if the account is active",
    )
