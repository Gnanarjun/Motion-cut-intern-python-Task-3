import datetime

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    
    if date not in expenses:
        expenses[date] = []
    
    expenses[date].append({"amount": amount, "category": category})
    
    print("Expense added successfully!")

def monthly_summary(year, month):
    total = 0
    for date, expenses_list in expenses.items():
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
        if date_obj.year == year and date_obj.month == month:
            for expense in expenses_list:
                total += expense["amount"]
    return total

def category_wise_summary(category):
    total = 0
    for date, expenses_list in expenses.items():
        for expense in expenses_list:
            if expense["category"] == category:
                total += expense["amount"]
    return total

def main_menu():
    while True:
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_expense()
        elif choice == 2:
            year = int(input("Enter the year: "))
            month = int(input("Enter the month: "))
            print("Total expenses:", monthly_summary(year, month))
        elif choice == 3:
            category = input("Enter the category: ")
            print("Total expenses:", category_wise_summary(category))
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

expenses = {}
categories = ["Food", "Transportation", "Utilities", "Entertainment", "Shopping"]

try:
    main_menu()
except ValueError:
    print("Invalid input. Please enter a valid number.")
except KeyError:
    print("Invalid date format. Please use YYYY-MM-DD.")