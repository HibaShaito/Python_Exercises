"""
In this section, we will introduce two projects

🧠 Project 1 – Expense Tracker CLI App
| A full program combining file I/O, classes, user input, conditionals, lists, and dictionaries. 📌 Objective:

Create a command-line expense tracker where users can:

Add a new expense (category, amount, date)
View all expenses
View total spent per category
Save & load expenses from a CSV file
🧩 Features:

Expense class: holds category, amount, date
ExpenseManager class:
.add_expense()
.view_expenses()
.category_summary()
.save_to_csv() and .load_from_csv()
| Note: You can skip the hard section until you finish the Machine Learning Practice Course, Because it includes the libraries that you want to work with in order to read and write csv, such as Pandas

As a Hint, If you want to read and write CSV file (Excel, but delimited with comma instead of columns of the excel) Use the following snippets:

import pandas as pd
df = pd.reas_csv("file/path/here") #df is dataframe, everything is explained in Course 5

#if you want to write a dataframe to CSV file
df.to_csv("file/to/save/here")
"""
import pandas as pd
import os

class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"Expense Category: {self.category}, Expense Amount: {self.amount}, Expense Date: {self.date}"


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def view_expenses(self):
        for expense in self.expenses:
            print(expense)

    def category_summary(self):
        summary = {}
        for expense in self.expenses:
            if expense.category in summary:
                summary[expense.category] += expense.amount
            else:
                summary[expense.category] = expense.amount

        for cat, amount in summary.items():
            print(f"Category: {cat} -> Amount Spent: {amount}")

    def save_to_csv(self, path):
        """Save the expenses list to a CSV file."""
        data = {
            "category": [expense.category for expense in self.expenses],
            "amount": [expense.amount for expense in self.expenses],
            "date": [expense.date for expense in self.expenses]
        }

        df = pd.DataFrame(data)
        df.to_csv(path, index=False)
        print(f"Saved expenses to {path}")

    def load_from_csv(self, path):
        """Load expenses from a CSV file and recreate Expense objects."""
        if not os.path.exists(path):
            print("CSV file not found!")
            return

        df = pd.read_csv(path)

        self.expenses = []  # reset
        for _, row in df.iterrows():
            expense = Expense(
                category=row["category"],
                amount=row["amount"],
                date=row["date"]
            )
            self.expenses.append(expense)

        print(f"Loaded {len(self.expenses)} expenses from {path}")


# --------------------- TESTING ---------------------

if __name__ == "__main__":
    manager = ExpenseManager()

    # Load existing CSV if you want
    manager.load_from_csv("3_hard/data.csv")

    # Add new expenses
    e1 = Expense("cheese", 40, "17-2-2025")
    e2 = Expense("milk", 80, "12-5-2025")
    e3 = Expense("cheese", 90, "18-2-2025")

    manager.add_expense(e1)
    manager.add_expense(e2)
    manager.add_expense(e3)

    manager.category_summary()
    manager.view_expenses()

    # Save updated CSV
    manager.save_to_csv("3_hard/data.csv")
