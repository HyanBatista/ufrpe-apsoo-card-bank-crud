from datetime import date

from app.db.models.card import CreditCard
from app.db.repositories.card import CardRepository
from app.schemas.card import CardCreate, CardRead


class CreateCardService:
    def __init__(self, repository: CardRepository):
        self.repository = repository

    def exec(self, data: CardCreate) -> CardRead:
        """Create a new credit card."""
        credit_card: CreditCard = self.repository.create(
            number=data.number,
            holder=data.holder,
            expiration=date.fromisoformat(data.expiration),
            cvv=data.cvv,
        )
        card_read_schema = CardRead.model_validate(
            {
                "id": credit_card.id,
                "number": credit_card.number,
                "holder": credit_card.holder,
                "expiration": (
                    credit_card.expiration.isoformat()
                    if isinstance(credit_card.expiration, date)
                    else credit_card.expiration
                ),
                "cvv": credit_card.cvv,
                "credit_limit": credit_card.credit_limit,
                "is_active": credit_card.is_active,
            }
        )
        return card_read_schema


class ReadCardService:
    def __init__(self, repository: CardRepository):
        self.repository = repository

    def exec(self, skip: int = 0, limit: int = 10) -> list[CardRead]:
        """Retrieve all credit cards."""
        cards = self.repository.get_all(skip=skip, offset=limit)
        return [
            CardRead.model_validate(
                {
                    "id": card.id,
                    "number": card.number,
                    "holder": card.holder,
                    "expiration": (
                        card.expiration.isoformat()
                        if hasattr(card.expiration, "isoformat")
                        else card.expiration
                    ),
                    "cvv": card.cvv,
                    "credit_limit": card.credit_limit,
                    "is_active": card.is_active,
                }
            )
            for card in cards
        ]
