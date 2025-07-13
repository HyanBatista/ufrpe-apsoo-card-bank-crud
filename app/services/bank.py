from app.schemas.bank import BankAccountCreate, BankAccountRead
from app.db.repositories.bank import BankAccountRepository
from app.db.models.bank import BankAccount


class CreateBankAccountService:
    def __init__(self, repository: BankAccountRepository):
        self.repository = repository

    def exec(self, data: BankAccountCreate) -> BankAccountRead:
        """Create a new bank account."""
        bank_account: BankAccount = self.repository.create(
            owner_name=data.owner_name,
            account_number=data.account_number,
            balance=data.balance,
        )
        bank_count_read_schema = BankAccountRead.model_validate(bank_account)
        return bank_count_read_schema


class ReadBankAccountService:
    def __init__(self, repository: BankAccountRepository):
        self.repository = repository

    def exec(self, skip: int = 0, limit: int = 10) -> list[BankAccountRead]:
        """Retrieve all bank accounts."""
        accounts = self.repository.get_all(skip=skip, offset=limit)
        return [BankAccountRead.model_validate(account) for account in accounts]
