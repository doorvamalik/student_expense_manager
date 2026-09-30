from collections import defaultdict
from .database import list_expenses

def total_expenses(rows=None):
    rows = list_expenses() if rows is None else rows
    return sum(row[2] for row in rows)

def category_summary(rows=None):
    rows = list_expenses() if rows is None else rows
    summary = defaultdict(float)
    for row in rows: summary[row[3]] += row[2]
    return dict(sorted(summary.items(), key=lambda item: item[1], reverse=True))

def monthly_summary(rows=None):
    rows = list_expenses() if rows is None else rows
    summary = defaultdict(float)
    for row in rows: summary[row[4][:7]] += row[2]
    return dict(sorted(summary.items()))

def highest_category(rows=None):
    summary = category_summary(rows)
    return max(summary.items(), key=lambda x: x[1]) if summary else None
