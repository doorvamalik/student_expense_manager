from datetime import datetime

def validate_expense(title, amount, category, expense_date):
    errors = []
    if not title.strip(): errors.append("Title is required.")
    if not category.strip(): errors.append("Category is required.")
    try:
        value = float(amount)
        if value <= 0: errors.append("Amount must be greater than 0.")
    except (TypeError, ValueError):
        errors.append("Amount must be a valid number.")
    try:
        datetime.strptime(expense_date, "%Y-%m-%d")
    except ValueError:
        errors.append("Date must use YYYY-MM-DD format.")
    return errors
