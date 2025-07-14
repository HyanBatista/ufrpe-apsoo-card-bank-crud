from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.repositories.card import CreditCardRepository
from app.db.session import get_session
from app.schemas.card import CreditCardCreate, CreditCardRead
from app.services.card import CreateCreditCardService, ReadCreditCardService

router = APIRouter(
    prefix="/card",
    tags=["card"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[CreditCardRead])
def read_credit_cards(
    skip: int = 0, limit: int = 10, session: Session = Depends(get_session)
):
    """Retrieve all credit cards."""
    cards = ReadCreditCardService(repository=CreditCardRepository(session=session)).exec(
        skip=skip, limit=limit
    )
    return cards


@router.post("/", response_model=CreditCardRead)
def create_credit_card(card: CreditCardCreate, session: Session = Depends(get_session)):
    """Create a new credit card."""
    card_read: CreditCardRead = CreateCreditCardService(
        repository=CreditCardRepository(session=session)
    ).exec(data=card)
    return card_read
