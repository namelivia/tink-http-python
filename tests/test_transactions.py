from tink_http_python.transactions import Transactions


class TestTransactions:
    def test_get(self):
        transactions = Transactions.get()
