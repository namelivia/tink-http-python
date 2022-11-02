import csv

# Quick and dirty category manager


def get_category(description):
    with open('categories') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if description in row[1:]:
                return row[0]
        return None


def get_all_categories():
    with open('categories') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        return [row[0] for row in spamreader]
