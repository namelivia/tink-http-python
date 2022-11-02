from cat.categories import get_all_categories

# Quick and dirty UI


def get_memo():
    print("Please enter a memo:")
    return input()


def should_add_to_existing():
    answer = "Z"
    while answer not in "YyNn":
        print("Do you want to add it to an existing category?(Y/N)")
        answer = input()
    return answer in "Yy"


def ask_category():
    categories = get_all_categories()
    answer = -1
    while answer < 0 or answer > len(categories):
        display_categories(categories)
        print("Please choose the category:")
        answer = int(input())
    return categories[answer]


def display_categories(categories):
    for index, category in enumerate(categories):
        print(f"{index}: {category}")
