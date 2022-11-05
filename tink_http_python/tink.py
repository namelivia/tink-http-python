from .api import ApiV1, ApiV2
from .accounts import Accounts
from .transactions import Transactions
from .authentication.authentication import Authentication
from .authentication.storage import Storage
from .config import Config


class Tink:
    def __init__(self, *, client_id: str, client_secret: str, storage: Storage):
        config = Config(client_id=client_id, client_secret=client_secret)
        apiV2 = ApiV2()
        authentication = Authentication(ApiV1(), storage, config)
        self._apiV1 = ApiV2()
        self._accounts = Accounts(apiV2, authentication)
        self._transactions = Transactions(apiV2, authentication)

    def accounts(self):
        return self._accounts

    def transactions(self):
        return self._transactions
