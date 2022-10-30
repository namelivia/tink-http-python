from .storage import Storage
from .api import Api
import os


class Authentication:
    def __init__(self):
        self.storage = Storage()
        self.api = Api()

    def _get_tink_link():
        client_id = os.environ.get("TINK_CLIENT_ID")
        return f"https://link.tink.com/1.0/transactions/connect-accounts/?client_id={client_id}&redirect_uri=https%3A%2F%2Fconsole.tink.com%2Fcallback&market=ES&locale=es_ES"

    def get_refresh_token(self) -> str:
        # This is only needed if there is no referesh token
        print(self.get_tink_link(os.environ.get("TINK_CLIENT_ID")))
        code = input()
        token_response = self.api.get_new_access_token(
            os.environ.get("TINK_CLIENT_ID"),
            os.environ.get("TINK_CLIENT_SECRET"),
            code
        ).json()
        self.storage.store_new_refresh_token_refresh_token(token_response["refresh_token"])

    def get_access_token(self) -> str:
        refresh_token = self.storage.retrieve_refresh_token()
        token_response = self.api.refresh_token(
            os.environ.get("TINK_CLIENT_ID"),
            os.environ.get("TINK_CLIENT_SECRET"),
            refresh_token
        ).json()
        self.storage.store_new_refresh_token_refresh_token(token_response["refresh_token"])
        return token_response["access_token"]
