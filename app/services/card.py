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


class UpdateCreditCardService:
    def __init__(self, repository: CreditCardRepository):
        self.repository = repository

    def exec(
        self,
        card_id: int,
        number: str | None = None,
        holder: str | None = None,
        expiration: date | None = None,
        cvv: str | None = None,
        credit_limit: float | None = None,
    ) -> CreditCardRead | None:
        """Update an existing credit card."""
        updated_card = self.repository.update(
            card_id=card_id,
            number=number,
            holder=holder,
            expiration=expiration,
            cvv=cvv,
            credit_limit=credit_limit,
        )
        if updated_card:
            return CreditCardRead.model_validate(updated_card.model_dump())
        return None


class DeleteCreditCardService:
    def __init__(self, repository: CreditCardRepository):
        self.repository = repository

    def exec(self, card_id: int) -> bool:
        """Delete a credit card by its ID."""
        return self.repository.delete(card_id=card_id)
