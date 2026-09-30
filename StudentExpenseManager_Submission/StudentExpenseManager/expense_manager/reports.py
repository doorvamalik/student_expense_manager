from .services import total_expenses, category_summary, monthly_summary

def build_report(rows):
    lines = ["STUDENT EXPENSE REPORT", "=" * 50]
    lines.append(f"Total spending: INR {total_expenses(rows):.2f}")
    lines.append("\nBy category:")
    for category, amount in category_summary(rows).items():
        lines.append(f"  - {category}: INR {amount:.2f}")
    lines.append("\nBy month:")
    for month, amount in monthly_summary(rows).items():
        lines.append(f"  - {month}: INR {amount:.2f}")
    lines.append("\nTransactions:")
    for row in rows:
        lines.append(f"  #{row[0]} | {row[4]} | {row[3]} | {row[1]} | INR {row[2]:.2f}")
    return "\n".join(lines)
