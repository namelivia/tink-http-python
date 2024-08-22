from .storage import Storage
from tink_http_python.api import ApiV1
from tink_http_python.config import Config
from tink_http_python.exceptions import (
    NoAuthorizationCodeException,
    NoAccessTokenException,
)
from urllib.parse import quote_plus
from .api import Api


class Authentication:
    def __init__(self, api: ApiV1, storage: Storage, config: Config):
        self.storage = storage
        self.api = Api(api)
        self.config = config

    def get_authorization_code_link(self):
        link = quote_plus(self.config.redirect_uri)

        return f"https://link.tink.com/1.0/transactions/connect-accounts/?client_id={self.config.client_id}&redirect_uri={link}&market=ES&locale=es_ES"

    def _get_new_access_token(self) -> str:
        code = self.storage.retrieve_authorization_code()
        token_response = self.api.get_new_access_token(
            self.config.client_id, self.config.client_secret, code
        )
        return token_response["access_token"]

    def get_access_token(self) -> str:
        try:
            return self.storage.retrieve_access_token()
        except NoAccessTokenException:
            new_access_token = self._get_new_access_token()
            self.storage.store_new_access_token(new_access_token)
            return new_access_token
