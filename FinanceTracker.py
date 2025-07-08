import datetime

expenses = []

def add_expense(amount, category, date=None):
    if date is None:
        date = datetime.date.today().isoformat()
    expenses.append({"amount": amount, "category": category, "date": date})
    print(f"Added ${amount:.2f} to {category} on {date}")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nAll Expenses:")
    for idx, exp in enumerate(expenses):
        print(f"{idx}. ${exp['amount']:.2f} - {exp['category']} on {exp['date']}")

def view_summary():
    summary = {}
    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]
    print("\nSpending Summary:")
    for cat, total in summary.items():
        print(f"{cat}: ${total:.2f}")

def delete_expense(index):
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted: ${removed['amount']:.2f} - {removed['category']} on {removed['date']}")
    else:
        print("Invalid index.")

def edit_expense(index):
    if 0 <= index < len(expenses):
        try:
            amount = float(input("Enter new amount: "))
            category = input("Enter new category: ")
            date = input("Enter new date (YYYY-MM-DD) or leave blank for today: ").strip()
            if not date:
                date = datetime.date.today().isoformat()
            expenses[index] = {"amount": amount, "category": category, "date": date}
            print("Expense updated.")
        except ValueError:
            print("Invalid input.")
    else:
        print("Invalid index.")

def save_to_file():
    with open("expenses.txt", "w") as file:
        for exp in expenses:
            file.write(f"{exp['amount']},{exp['category']},{exp['date']}\n")
    print("Expenses saved!")

def load_from_file():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category, date = line.strip().split(",")
                expenses.append({
                    "amount": float(amount),
                    "category": category,
                    "date": date
                })
    except FileNotFoundError:
        pass  # No saved data yet

def search_expenses():
    keyword = input("Enter category or date (YYYY-MM-DD) to search: ").strip().lower()
    results = [exp for exp in expenses if keyword in exp["category"].lower() or keyword == exp["date"]]
    
    if results:
        print("\nSearch Results:")
        for idx, exp in enumerate(results):
            print(f"{idx}. ${exp['amount']:.2f} - {exp['category']} on {exp['date']}")
    else:
        print("No matching expenses found.")

def sort_expenses():
    print("Sort by: 1) Date (latest first), 2) Amount (highest first)")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        sorted_list = sorted(expenses, key=lambda x: x["date"], reverse=True)
    elif choice == "2":
        sorted_list = sorted(expenses, key=lambda x: x["amount"], reverse=True)
    else:
        print("Invalid choice.")
        return

    print("\nSorted Expenses:")
    for idx, exp in enumerate(sorted_list):
        print(f"{idx}. ${exp['amount']:.2f} - {exp['category']} on {exp['date']}")

def main():
    load_from_file()
    print("Personal Finance Tracker (type 'exit' to quit)")
    while True:
        action = input("Choose: add, view, summary, edit, delete, search, sort, save, exit: ").lower()
        if action == "exit":
            print("Goodbye!")
            break
        elif action == "add":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (e.g., food, books): ")
                date = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
                date = date if date else None
                add_expense(amount, category, date)
            except ValueError:
                print("Invalid amount.")
        elif action == "view":
            view_expenses()
        elif action == "summary":
            view_summary()
        elif action == "delete":
            view_expenses()
            try:
                index = int(input("Enter index to delete: "))
                delete_expense(index)
            except ValueError:
                print("Invalid index.")
        elif action == "edit":
            view_expenses()
            try:
                index = int(input("Enter index to edit: "))
                edit_expense(index)
            except ValueError:
                print("Invalid index.")
        elif action == "search":
            search_expenses()
        elif action == "sort":
            sort_expenses()
        elif action == "save":
            save_to_file()
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
