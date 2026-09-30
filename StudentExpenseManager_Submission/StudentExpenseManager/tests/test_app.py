import unittest
from expense_manager.validators import validate_expense
from expense_manager.services import total_expenses, category_summary

class TestExpenseManager(unittest.TestCase):
    def test_validation(self):
        self.assertEqual(validate_expense("Food", "120", "Food", "2026-09-30"), [])
        self.assertTrue(validate_expense("", "-10", "", "bad-date"))
    def test_total(self):
        rows = [(1,"Food",100.0,"Food","2026-09-30",""),(2,"Bus",50.0,"Travel","2026-09-30","")]
        self.assertEqual(total_expenses(rows), 150.0)
    def test_category_summary(self):
        rows = [(1,"Food",100.0,"Food","2026-09-30",""),(2,"Lunch",50.0,"Food","2026-09-30","")]
        self.assertEqual(category_summary(rows)["Food"], 150.0)

if __name__ == "__main__": unittest.main()
