from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.repositories.card import CardRepository
from app.db.session import get_session
from app.schemas.card import CardCreate, CardRead
from app.services.card import CreateCardService, ReadCardService

router = APIRouter(
    prefix="/card",
    tags=["card"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[CardRead])
def read_credit_cards(
    skip: int = 0, limit: int = 10, session: Session = Depends(get_session)
):
    """Retrieve all credit cards."""
    cards = ReadCardService(repository=CardRepository(session=session)).exec(
        skip=skip, limit=limit
    )
    return cards


@router.post("/", response_model=CardRead)
def create_credit_card(card: CardCreate, session: Session = Depends(get_session)):
    """Create a new credit card."""
    card_read: CardRead = CreateCardService(
        repository=CardRepository(session=session)
    ).exec(data=card)
    return card_read
