import os
import json
from tink_http_python.transactions import Transactions
from tink_http_python.authentication.authentication import Authentication
from tink_http_python.api import ApiV2
from mock import Mock


class TestTransactions:
    def setup_method(self):
        self.api = Mock(spec=ApiV2)
        self.authentication = Mock(spec=Authentication)
        self.transactions = Transactions(self.api, self.authentication)

    def get_stub_contents(self, stub_name):
        path = os.path.join(os.path.dirname(__file__), "./stubs/")
        with open(path + stub_name) as stub_data:
            return json.load(stub_data)

    def assert_equals_transactions_stub(self, transactions_page):
        # TODO: All the commented out values are optional
        assert transactions_page.next_page_token == "string"
        assert len(transactions_page.transactions) == 1
        assert (
            transactions_page.transactions[0].account_id
            == "4a2945d1481c4f4b98ab1b135afd96c0"
        )
        assert transactions_page.transactions[0].amount.currency_code == "GBP"
        assert transactions_page.transactions[0].amount.value.scale == "1"
        assert transactions_page.transactions[0].amount.value.unscaled_value == "-1300"
        # assert transactions_page.transactions[0].booked_date_time == "2020-12-15T09:25:12Z"
        assert (
            transactions_page.transactions[0].categories.pfm.id
            == "d8f37f7d19c240abb4ef5d5dbebae4ef"
        )
        assert transactions_page.transactions[0].categories.pfm.name == ""
        assert transactions_page.transactions[0].dates.booked == "2020-12-15"
        assert transactions_page.transactions[0].dates.value == "2020-12-15"
        assert transactions_page.transactions[0].descriptions.display == "Tesco"
        assert (
            transactions_page.transactions[0].descriptions.original
            == "TESCO STORES 3297"
        )
        assert (
            transactions_page.transactions[0].id == "d8f37f7d19c240abb4ef5d5dbebae4ef"
        )
        # assert transactions_page.transactions[0].identifiers.provider_transaction_id == "500015d3-acf3-48cc-9918-9e53738d3692"
        # assert transactions_page.transactions[0].merchant_information.merchantCategoryCode == "string"
        # assert transactions_page.transactions[0].merchant_information.merchantName == "string"
        assert (
            transactions_page.transactions[0].provider_mutability
            == "MUTABILITY_UNDEFINED"
        )
        assert transactions_page.transactions[0].reference == "string"
        assert transactions_page.transactions[0].status == "BOOKED"
        # assert transactions_page.transactions[0].transaction_date_time == "string"
        # assert transactions_page.transactions[0].types.financial_institution_type_code == "DEB"
        assert transactions_page.transactions[0].types.type == "DEFAULT"
        # assert transactions_page.transactions[0].value_date_time == "2020-12-15T09:25:12Z"

    def test_get(self):
        self.api.get.return_value = self.get_stub_contents("transactions.json")
        self.authentication.get_access_token.return_value = "Access token"
        transactions = self.transactions.get()
        self.api.get.assert_called_once_with(
            "transactions", {"Authorization": "Bearer Access token"}
        )
        self.assert_equals_transactions_stub(transactions)
