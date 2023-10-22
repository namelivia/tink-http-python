from tink_http_python.api import ApiV1


class Api:
    def __init__(self, api: ApiV1):
        self.api = api

    def refresh_token(self, client_id, client_secret, token) -> dict:
        return self.api.post(
            "oauth/token",
            {},
            {
                "client_id": client_id,
                "refresh_token": token,
                "client_secret": client_secret,
                "grant_type": "refresh_token",
            },
        )

    def get_new_access_token(self, client_id, client_secret, code) -> dict:
        return self.api.post(
            "oauth/token",
            {},
            {
                "client_id": client_id,
                "code": code,
                "client_secret": client_secret,
                "grant_type": "authorization_code",
            },
        )
