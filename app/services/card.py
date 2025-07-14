from datetime import date

from app.db.models.card import CreditCard
from app.db.repositories.card import CreditCardRepository
from app.schemas.card import CreditCardCreate, CreditCardRead


class CreateCreditCardService:
    def __init__(self, repository: CreditCardRepository):
        self.repository = repository

    def exec(self, data: CreditCardCreate) -> CreditCardRead:
        """Create a new credit card."""
        credit_card: CreditCard = self.repository.create(
            number=data.number,
            holder=data.holder,
            expiration=data.expiration,
            cvv=data.cvv,
            credit_limit=data.credit_limit,
            account_id=data.account_id,
        )
        return CreditCardRead.model_validate(credit_card.model_dump())


class ReadCreditCardService:
    def __init__(self, repository: CreditCardRepository):
        self.repository = repository

    def exec(self, skip: int = 0, limit: int = 10) -> list[CreditCardRead]:
        """Retrieve all credit cards."""
        cards = self.repository.get_all(skip=skip, offset=limit)
        return [CreditCardRead.model_validate(card.model_dump()) for card in cards]
