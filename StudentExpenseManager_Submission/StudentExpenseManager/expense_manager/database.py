import sqlite3
from pathlib import Path
from .config import DB_NAME

DB_PATH = Path(__file__).resolve().parent.parent / DB_NAME

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL CHECK(amount > 0),
            category TEXT NOT NULL,
            expense_date TEXT NOT NULL,
            notes TEXT DEFAULT ''
        )''')
        conn.commit()

def add_expense(title, amount, category, expense_date, notes=""):
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO expenses(title, amount, category, expense_date, notes) VALUES (?, ?, ?, ?, ?)",
            (title, amount, category, expense_date, notes))
        conn.commit()
        return cur.lastrowid

def list_expenses():
    with get_connection() as conn:
        return conn.execute(
            "SELECT id, title, amount, category, expense_date, notes FROM expenses ORDER BY expense_date DESC, id DESC"
        ).fetchall()

def delete_expense(expense_id):
    with get_connection() as conn:
        cur = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        return cur.rowcount

def update_expense(expense_id, title, amount, category, expense_date, notes=""):
    with get_connection() as conn:
        cur = conn.execute(
            "UPDATE expenses SET title=?, amount=?, category=?, expense_date=?, notes=? WHERE id=?",
            (title, amount, category, expense_date, notes, expense_id))
        conn.commit()
        return cur.rowcount
