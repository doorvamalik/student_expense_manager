# Design Decisions & Requirements

## Functional Requirements
1. Add an expense.
2. View stored expenses.
3. Update an expense.
4. Delete an expense.
5. Calculate total and category/month summaries.
6. Generate a readable report.

## Non-Functional Requirements
1. Usability: menu-driven interface with clear prompts.
2. Reliability: SQLite transactions are committed after changes.
3. Maintainability: separate modules for database, validation, services, reports and UI.
4. Error handling: invalid amounts, dates, empty fields and IDs are handled safely.
5. Performance: SQLite operations are appropriate for student-scale data.
6. Resource efficiency: Python standard library only; no external server.

## Rationale
SQLite was selected because it is built into Python, requires no server setup, and provides persistent structured storage. Modular separation makes individual components easier to test and maintain.
