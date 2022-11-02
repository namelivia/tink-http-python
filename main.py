import csv
from pkg.transactions.transactions import Transactions
from cat.categories import get_category
from ui.ui import get_memo, should_add_to_existing, ask_category


transactions = Transactions().get()

with open('output.csv', 'w') as f:
    writer = csv.writer(f,  delimiter=';')
    for transaction in transactions.transactions:
        category = get_category(transaction.descriptions.original)
        memo = ""
        if category is None:
            Transactions.render(transaction)
            if should_add_to_existing():
                category = ask_category()
            else:
                memo = get_memo()
        writer.writerow((
            transaction.dates.value,
            0,
            transaction.descriptions.original,
            None,
            memo,
            Transactions.calculate_real_amount(transaction.amount.value),
            category,
            None
        ))
