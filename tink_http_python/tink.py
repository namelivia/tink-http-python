from .accounts import Accounts
from .transactions import Transactions


class Tink:
    def __init__(self):
        self._accounts = Accounts()
        self._transactions = Transactions()

    def accounts(self):
        return self._accounts

    def transactions(self):
        return self._transactions
