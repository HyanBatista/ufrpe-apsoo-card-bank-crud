from datetime import date

from sqlmodel import Session, select

from app.db.models.card import CreditCard


class CreditCardRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        number: str,
        holder: str,
        expiration: date,
        cvv: str,
        credit_limit: float,
        account_id: int,
    ) -> CreditCard:
        """Create a new credit card."""
        card = CreditCard(
            number=number,
            holder=holder,
            experation=expiration,
            cvv=cvv,
            credit_limit=credit_limit,
            account_id=account_id,
        )
        self.session.add(card)
        self.session.commit()
        self.session.refresh(card)
        return card

    def get_all(self, skip=0, offset=10) -> list[CreditCard]:
        """Retrieve all credit cards."""
        return self.session.exec(select(CreditCard).offset(skip).limit(offset)).all()

    def get_by_id(self, card_id: int) -> CreditCard | None:
        """Retrieve a credit card by its ID."""
        return self.session.get(CreditCard, card_id)
