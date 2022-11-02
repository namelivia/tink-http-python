from pydantic.dataclasses import dataclass
from pkg.common import Amount
from typing import List


@dataclass
class Balance:
    amount: Amount


@dataclass
class Balances:
    booked: Balance
    available: Balance


@dataclass
class Iban:
    iban: str
    bban: str


@dataclass
class FinancialInstitution:
    account_number: str
    # reference_numbers: any


@dataclass
class Identifiers:
    iban: Iban
    financial_institution: FinancialInstitution


@dataclass
class Dates:
    last_refreshed: str


@dataclass
class Account:
    id: str
    name: str
    type: str
    balances: Balances
    identifiers: Identifiers
    dates: Dates
    financial_institution_id: str
    customer_segment: str


@dataclass
class AccountsPage:
    accounts: List[Account]
    next_page_token: str
