from pydantic.dataclasses import dataclass
from pkg.common import Amount
from typing import List


@dataclass
class PFM:
    id: str
    name: str


@dataclass
class Categories:
    pfm: PFM


@dataclass
class Types:
    type: str


@dataclass
class Dates:
    booked: str
    value: str


@dataclass
class Descriptions:
    original: str
    display: str


@dataclass
class Transaction:
    id: str
    account_id: str
    amount: Amount
    descriptions: Descriptions
    dates: Dates
    types: Types
    categories: Categories
    status: str
    provider_mutability: str
    reference: str = None


@dataclass
class TransactionsPage:
    transactions: List[Transaction]
    next_page_token: str
