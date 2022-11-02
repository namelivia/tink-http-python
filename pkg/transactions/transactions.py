from pkg.api import ApiV2
from pkg.authentication.authentication import Authentication
from pkg.dataclass_wrapper.dataclass_wrapper import DataclassWrapper
import humps
from .transaction import TransactionsPage


class Transactions:
    def __init__(self):
        self.api = ApiV2()
        self.auth = Authentication()

    def get(self):
        return DataclassWrapper.wrap(
            TransactionsPage,
            humps.decamelize(self.api.get("transactions", {
                'Authorization': f"Bearer {self.auth.get_access_token()}"
            }).json())
        )

    @staticmethod
    def calculate_real_amount(value):
        return int(value.unscaled_value) / (10 ** int(value.scale))

    @staticmethod
    def render(transaction):
        print("==========================")
        print(transaction.dates.value)
        print(transaction.descriptions.original)
        print(Transactions.calculate_real_amount(transaction.amount.value))
        print("==========================")
