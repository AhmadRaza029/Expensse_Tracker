class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, date, category, amount):
        if date not in self.expenses:
            self.expenses[date] = {}
        if category not in self.expenses[date]:
            self.expenses[date][category] = 0
        self.expenses[date][category] += amount

    def view_expenses(self, date=None):
        if date:
            if date in self.expenses:
                print(f"Expenses on {date}:")
                for category, amount in self.expenses[date].items():
                    print(f"{category}: ${amount}")
            else:
                print("No expenses recorded for this date.")
        else:
            print("Total expenses:")
            for date, categories in self.expenses.items():
                print(f"On {date}:")
                for category, amount in categories.items():
                    print(f"{category}: ${amount}")
                print("")

    def view_spending_patterns(self, category=None):
        if category:
            total_spent = 0
            for date, categories in self.expenses.items():
                if category in categories:
                    total_spent += categories[category]
            print(f"Total spent on {category}: ${total_spent}")
        else:
            category_totals = {}
            for date, categories in self.expenses.items():
                for category, amount in categories.items():
                    if category not in category_totals:
                        category_totals[category] = 0
                    category_totals[category] += amount
            print("Spending patterns:")
            for category, total in category_totals.items():
                print(f"{category}: ${total}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Patterns")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            
            amount = float(input("Enter amount: $"))
            tracker.add_expense(date, category, amount)
        elif choice == "2":
            date = input("Enter date to view expenses (leave blank for all dates): ")
            tracker.view_expenses(date)
        elif choice == "3":
            category = input("Enter category to view spending pattern (leave blank for all categories): ")
            tracker.view_spending_patterns(category)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
