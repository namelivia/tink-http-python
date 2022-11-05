from .storage import Storage
from tink_http_python.api import ApiV1
from tink_http_python.config import Config
from .api import Api


class Authentication:
    def __init__(self, api: ApiV1, storage: Storage, config: Config):
        self.storage = storage
        self.api = Api(api)
        self.config = config

    def _get_tink_link(self):
        return f"https://link.tink.com/1.0/transactions/connect-accounts/?client_id={self.config.client_id}&redirect_uri=https%3A%2F%2Fconsole.tink.com%2Fcallback&market=ES&locale=es_ES"

    def get_refresh_token(self) -> str:
        try:
            code = self.storage.retrieve_authorization_code()
        except FileNotFoundError:
            print("Get a code from this link and save it as authorization_code:")
            print(self._get_tink_link())
            exit()
        token_response = self.api.get_new_access_token(
            self.config.client_id, self.config.client_secret, code
        )
        self.storage.store_new_refresh_token_refresh_token(
            token_response["refresh_token"]
        )

    def get_access_token(self) -> str:
        try:
            refresh_token = self.storage.retrieve_refresh_token()
        except FileNotFoundError:
            refresh_token = self.get_refresh_token()
        token_response = self.api.refresh_token(
            self.config.client_id,
            self.config.client_secret,
            refresh_token,
        )
        self.storage.store_new_refresh_token_refresh_token(
            token_response["refresh_token"]
        )
        return token_response["access_token"]
