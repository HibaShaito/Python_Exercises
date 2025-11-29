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