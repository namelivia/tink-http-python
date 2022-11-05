from .storage import Storage
from tink_http_python.api import ApiV1
from .api import Api
import os


class Authentication:
    def __init__(self, api: ApiV1, storage: Storage):
        self.storage = storage
        self.api = Api(api)

    def _get_tink_link(self):
        client_id = os.environ.get("TINK_CLIENT_ID")
        return f"https://link.tink.com/1.0/transactions/connect-accounts/?client_id={client_id}&redirect_uri=https%3A%2F%2Fconsole.tink.com%2Fcallback&market=ES&locale=es_ES"

    def get_refresh_token(self) -> str:
        try:
            code = self.storage.retrieve_authorization_code()
        except FileNotFoundError:
            print("Get a code from this link and save it as authorization_code:")
            print(self._get_tink_link())
            exit()
        token_response = self.api.get_new_access_token(
            os.environ.get("TINK_CLIENT_ID"), os.environ.get("TINK_CLIENT_SECRET"), code
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
            os.environ.get("TINK_CLIENT_ID"),
            os.environ.get("TINK_CLIENT_SECRET"),
            refresh_token,
        )
        self.storage.store_new_refresh_token_refresh_token(
            token_response["refresh_token"]
        )
        return token_response["access_token"]
