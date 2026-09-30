from datetime import date
from .database import init_db, add_expense, list_expenses, delete_expense, update_expense
from .validators import validate_expense
from .services import total_expenses, category_summary
from .reports import build_report

def read_expense_details(existing=None):
    if existing:
        title = input(f"Title [{existing[1]}]: ").strip() or existing[1]
        amount = input(f"Amount [{existing[2]}]: ").strip() or str(existing[2])
        category = input(f"Category [{existing[3]}]: ").strip() or existing[3]
        expense_date = input(f"Date [{existing[4]}]: ").strip() or existing[4]
        notes = input(f"Notes [{existing[5]}]: ").strip() or existing[5]
    else:
        title = input("Title: ").strip()
        amount = input("Amount (INR): ").strip()
        category = input("Category: ").strip()
        expense_date = input("Date (YYYY-MM-DD): ").strip() or str(date.today())
        notes = input("Notes (optional): ").strip()
    errors = validate_expense(title, amount, category, expense_date)
    if errors:
        print("\nValidation errors:")
        for error in errors: print("-", error)
        return None
    return title, float(amount), category, expense_date, notes

def show_expenses():
    rows = list_expenses()
    if not rows:
        print("\nNo expenses recorded yet."); return rows
    print("\nID | Date       | Category      | Title                 | Amount")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]:2} | {row[4]:10} | {row[3]:13} | {row[1][:20]:20} | INR {row[2]:8.2f}")
    print(f"\nTotal: INR {total_expenses(rows):.2f}")
    return rows

def main():
    init_db()
    while True:
        print("\n=== STUDENT EXPENSE MANAGER ===")
        print("1. Add expense\n2. View expenses\n3. Update expense\n4. Delete expense\n5. Analytics\n6. Generate report\n7. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            data = read_expense_details()
            if data: add_expense(*data); print("Expense added successfully.")
        elif choice == "2": show_expenses()
        elif choice == "3":
            rows = show_expenses()
            if rows:
                try:
                    expense_id = int(input("Enter ID to update: "))
                    existing = next((r for r in rows if r[0] == expense_id), None)
                    if not existing: print("Expense not found.")
                    else:
                        data = read_expense_details(existing)
                        if data: update_expense(expense_id, *data); print("Expense updated successfully.")
                except ValueError: print("Please enter a valid numeric ID.")
        elif choice == "4":
            rows = show_expenses()
            if rows:
                try:
                    expense_id = int(input("Enter ID to delete: "))
                    print("Deleted." if delete_expense(expense_id) else "Expense not found.")
                except ValueError: print("Please enter a valid numeric ID.")
        elif choice == "5":
            rows = list_expenses()
            print(f"\nTotal spending: INR {total_expenses(rows):.2f}")
            print("Category summary:")
            for category, amount in category_summary(rows).items(): print(f"  {category}: INR {amount:.2f}")
        elif choice == "6": print("\n" + build_report(list_expenses()))
        elif choice == "7": print("Goodbye!"); break
        else: print("Invalid option. Choose 1-7.")

if __name__ == "__main__": main()
