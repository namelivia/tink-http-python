from tink_http_python.api import ApiV2
from tink_http_python.authentication.authentication import Authentication
from dataclass_map_and_log.mapper import DataclassMapper
import humps
from tink_python_api_types.transaction import TransactionsPage


class Transactions:
    def __init__(self, api: ApiV2, auth: Authentication):
        self.api = api
        self.auth = auth

    def get(self):
        return DataclassMapper.map(
            TransactionsPage,
            humps.decamelize(
                self.api.get(
                    "transactions",
                    {"Authorization": f"Bearer {self.auth.get_access_token()}"},
                )
            ),
        )

    @staticmethod
    def calculate_real_amount(value):
        return int(value.unscaled_value) / (10 ** int(value.scale))
