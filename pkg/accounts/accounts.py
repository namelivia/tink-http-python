from pkg.api import ApiV2
from pkg.authentication.authentication import Authentication
from pkg.dataclass_wrapper.dataclass_wrapper import DataclassWrapper
import humps
from .account import AccountsPage


class Accounts:
    def __init__(self):
        self.api = ApiV2()
        self.auth = Authentication()

    def get(self):
        return DataclassWrapper.wrap(
            AccountsPage,
            humps.decamelize(self.api.get("accounts", {
                'Authorization': f"Bearer {self.auth.get_access_token()}"
            }).json())
        )
