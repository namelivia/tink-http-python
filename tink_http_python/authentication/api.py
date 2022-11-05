from pkg.api import ApiV1


class Api:
    def __init__(self):
        self.api = ApiV1()

    def refresh_token(self, client_id, client_secret, token) -> dict:  # GetAcessTokenResponse:

        response = self.api.post("oauth/token", {}, {
            'client_id': client_id,
            'refresh_token': token,
            'client_secret': client_secret,
            'grant_type': 'refresh_token'
        })
        if response.status_code == 200:
            return response
        print(response.__dict__)
        exit()

    def get_new_access_token(self, client_id, client_secret, code) -> dict:  # GetAcessTokenResponse:

        response = self.api.post("oauth/token", {}, {
            'client_id': client_id,
            'code': code,
            'client_secret': client_secret,
            'grant_type': 'authorization_code'
        })
        if response.status_code == 200:
            return response
        print(response.__dict__)
        exit()
