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
            expiration=data.expiration,
            cvv=data.cvv,
        )
        return CardRead.model_validate(credit_card.model_dump())


class ReadCardService:
    def __init__(self, repository: CardRepository):
        self.repository = repository

    def exec(self, skip: int = 0, limit: int = 10) -> list[CardRead]:
        """Retrieve all credit cards."""
        cards = self.repository.get_all(skip=skip, offset=limit)
        return [CardRead.model_validate(card.model_dump()) for card in cards]
