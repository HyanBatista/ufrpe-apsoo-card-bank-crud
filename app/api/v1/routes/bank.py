from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.repositories.bank import BankAccountRepository
from app.db.session import get_session
from app.schemas.bank import BankAccountCreate, BankAccountRead
from app.services.bank import CreateBankAccountService, ReadBankAccountService

router = APIRouter(
    prefix="/bank",
    tags=["bank"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[BankAccountRead])
def read_bank_accounts(
    skip: int = 0, limit: int = 10, session: Session = Depends(get_session)
):
    """Retrieve all bank accounts."""
    accounts = ReadBankAccountService(
        repository=BankAccountRepository(session=session)
    ).exec(skip=skip, limit=limit)
    return accounts


@router.post("/", response_model=BankAccountRead)
def create_bank_account(
    account: BankAccountCreate, session: Session = Depends(get_session)
):
    """Create a new bank account."""
    account: BankAccountRead = CreateBankAccountService(
        repository=BankAccountRepository(session=session)
    ).exec(data=account)
    return account
