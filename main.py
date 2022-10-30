from pkg.accounts import Accounts
from pkg.transactions import Transactions


print("ACCOUNTS")
res = Accounts().get()
print(res.json())

print("TRANSACTIONS")
res = Transactions().get()
print(res.json())
