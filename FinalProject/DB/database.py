import sqlite3
from Models.task import Task

DB_PATH = "tasks.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT,
            status TEXT
        )
        """
    )
    conn.commit()
    conn.close()

def insert_task(task):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, description, priority, status) VALUES (?, ?, ?, ?)",
        (task.title, task.description, task.priority, task.status)
    )

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, description, priority, status FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    tasks = []
    for row in rows:
        task = Task(row[0], row[1], row[2], row[3], row[4])
        tasks.append(task)

    return tasks

def update_task_status(task_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        (new_status, task_id)
    )

    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

    deleted = cursor.rowcount > 0
    conn.close()
    return deleted