# RemindMe: CLI Task Tracker with Automated Tagging

I built RemindMe to solve a personal pain point: managing tasks and metadata without leaving the terminal. Instead of using high-level frameworks, I built this from scratch using Python and MySQL to master the foundational mechanics of database connections and backend logic.

## The Tech Behind It
- **Logic:** Python 3
- **Database:** MySQL (Relational Database)
- **UI Formatting:** Tabulate library (for clean grid presentation)

## Key Logic & Features
1. **Automated Keyword Tagging:** The core business logic lies in `generate_auto_tags()`. It scans user input for custom keywords and auto-categorizes them into system tags like `#coding`, `#materi`, `#task`, etc., before hitting the database.
2. **Secure CRUD Operations:** Handled database connections using parameterized queries (`%s`) to prevent SQL injection, complete with robust error handling (`commit` and `rollback` mechanisms).
3. **Clean Database Architecture:** Designed structured tables with proper relational boundaries to ensure data integrity.

## What I Learned (The "Why")
This project allowed me to dive deep into backend architecture. Building the CRUD operations and connection handling manually forced me to think through query optimization and error states—skills that are essential for building reliable, production-ready systems.