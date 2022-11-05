from tink_http_python.accounts import Accounts
from tink_http_python.authentication.storage import Storage
from tink_http_python.transactions import Transactions
from tink_http_python.tink import Tink
from mock import Mock


class TestTink:
    def test_tink(self):
        storage = Mock(spec=Storage)
        tink = Tink(
            client_id="CLIENT_ID", client_secret="CLIENT_SECRET", storage=storage
        )
        assert type(tink.accounts()) == Accounts
        assert type(tink.transactions()) == Transactions
