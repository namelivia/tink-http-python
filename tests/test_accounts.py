from tink_http_python.accounts import Accounts


class TestAccounts:
    def test_get(self):
        accounts = Accounts.get()
