from .api import ApiV2
from .authentication.authentication import Authentication


class Accounts:
    def __init__(self):
        self.api = ApiV2()
        self.auth = Authentication()

    def get(self):
        return self.api.get("accounts", {
            'Authorization': f"Bearer {self.auth.get_access_token()}"
        })
