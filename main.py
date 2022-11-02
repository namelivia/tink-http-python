import csv
from pkg.transactions.transactions import Transactions
from pkg.categories import get_category


print("TRANSACTIONS")
transactions = Transactions().get()


def get_real_amount(value):
    return int(value.unscaled_value) / (10 * int(value.scale))


with open('output.csv', 'w') as f:
    writer = csv.writer(f,  delimiter=';')
    for transaction in transactions.transactions:
        category = get_category(transaction.descriptions.original)
        if category is None:
            print(transaction.descriptions.display)
        writer.writerow((
            transaction.dates.value,
            0,
            transaction.descriptions.display,
            None,
            "",  # memo
            get_real_amount(transaction.amount.value),
            category,
            None
        ))
