import os
import json
from tink_http_python.accounts import Accounts
from tink_http_python.authentication.authentication import Authentication
from tink_http_python.api import ApiV2
from mock import Mock


class TestAccounts:
    def setup_method(self):
        self.api = Mock(spec=ApiV2)
        self.authentication = Mock(spec=Authentication)
        self.accounts = Accounts(self.api, self.authentication)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "./stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def assert_equals_accounts_stub(self, accounts_page):
        # TODO: All the commented out values are optional
        assert accounts_page.accounts[0].balances.booked.amount.currency_code == "EUR"
        assert accounts_page.accounts[0].balances.booked.amount.value.scale == "-3"
        assert (
            accounts_page.accounts[0].balances.booked.amount.value.unscaled_value
            == "19"
        )
        assert (
            accounts_page.accounts[0].customer_segment == "UNDEFINED_CUSTOMER_SEGMENT"
        )
        assert accounts_page.accounts[0].dates.last_refreshed == "2020-12-15T12:16:58Z"
        assert (
            accounts_page.accounts[0].financial_institution_id
            == "6e68cc6287704273984567b3300c5822"
        )
        assert accounts_page.accounts[0].id == "ee7ddbd178494220bb184791783f4f63"
        # assert accounts_page.accounts[0].financial_institution.account_number == "SE6930000000011273547693"
        # assert accounts_page.accounts[0].iban.bban == "0000011273547693"
        # assert accounts_page.accounts[0].iban.iban == "SE6930000000011273547693"
        # assert accounts_page.accounts[0].pan.masked == "4000 12** **** 9010"
        assert accounts_page.accounts[0].name == "PERSONKONTO"
        assert accounts_page.accounts[0].type == "CHECKING"
        assert accounts_page.next_page_token == "string"

    def test_get(self):
        self.api.get.return_value = self.get_stub_contents("accounts.json")
        self.authentication.get_access_token.return_value = "Access token"
        accounts = self.accounts.get()
        self.api.get.assert_called_once_with(
            "accounts", {"Authorization": "Bearer Access token"}
        )
        self.assert_equals_accounts_stub(accounts)
