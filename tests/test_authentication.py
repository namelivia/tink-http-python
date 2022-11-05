from tink_http_python.accounts import Accounts


class TestAuthentication:
    def test_get(self):
        Accounts().get()
