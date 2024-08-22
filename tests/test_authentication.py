from tink_http_python.authentication.authentication import Authentication
from tink_http_python.authentication.storage import Storage
from tink_http_python.api import ApiV1
from tink_http_python.config import Config
from tink_http_python.exceptions import NoAccessTokenException
from mock import Mock


class TestAuthentication:
    def setup_method(self):
        self.api = Mock(spec=ApiV1)
        self.storage = Mock(spec=Storage)
        self.config = Config(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
            redirect_uri="https://RED.IRECT.URI/",
        )
        self.authentication = Authentication(self.api, self.storage, self.config)

    def test_get_existing_access_token(self):
        self.storage.retrieve_access_token.return_value = "ACCESS_TOKEN"
        access_token = self.authentication.get_access_token()
        assert access_token == "ACCESS_TOKEN"
        assert self.api.post.call_count == 0

    def test_get_new_access_token(self):
        self.storage.retrieve_access_token.side_effect = NoAccessTokenException
        self.storage.retrieve_authorization_code.return_value = "AUTHORIZATION_CODE"
        self.api.post.return_value = {"access_token": "ACCESS_TOKEN"}

        access_token = self.authentication.get_access_token()
        self.api.post.assert_called_once_with(
            "oauth/token",
            {},
            {
                "client_id": "CLIENT_ID",
                "code": "AUTHORIZATION_CODE",
                "client_secret": "CLIENT_SECRET",
                "grant_type": "authorization_code",
            },
        )
        assert access_token == "ACCESS_TOKEN"
        self.storage.store_new_access_token.assert_called_once_with("ACCESS_TOKEN")

    def test_get_authorization_code_link(self):
        link = self.authentication.get_authorization_code_link()
        assert (
            link
            == "https://link.tink.com/1.0/transactions/connect-accounts/?client_id=CLIENT_ID&redirect_uri=https%3A%2F%2FRED.IRECT.URI%2F&market=ES&locale=es_ES"
        )
