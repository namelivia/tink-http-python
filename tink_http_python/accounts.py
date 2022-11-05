from pkg.api import ApiV2
from pkg.authentication.authentication import Authentication
from dataclass_map_and_log.mapper import DataclassMapper
import humps
from tink_python_api_types.account import AccountsPage


class Accounts:
    def __init__(self):
        self.api = ApiV2()
        self.auth = Authentication()

    def get(self):
        return DataclassMapper.map(
            AccountsPage,
            humps.decamelize(self.api.get("accounts", {
                'Authorization': f"Bearer {self.auth.get_access_token()}"
            }).json())
        )
