import requests
from DB.database import (
    insert_task,
    get_all_tasks,
    update_task_status,
    delete_task,
)
from Models.task import Task

class MainController:
    def add_task(self, title, description, priority):
        task = Task(None, title, description, priority, "Open")
        new_id = insert_task(task)
        return new_id

    def list_tasks(self):
        return get_all_tasks()

    def change_task_status(self, task_id, new_status):
        return update_task_status(task_id, new_status)

    def remove_task(self, task_id):
        return delete_task(task_id)

    def get_ai_suggestion(self):
        tasks = get_all_tasks()
        if not tasks:
            return "There are no tasks yet. Add a task first."

        lines = []
        for t in tasks:
            lines.append(f"- (id={t.id}) {t.title} [{t.priority}] ({t.status})")
        tasks_text = "\n".join(lines)

        url = "http://localhost:11434/api/generate"

        payload = {
            "model": "llama3.1",
            "prompt": (
                "You are a to-do assistant.\n"
                "Here are my tasks:\n"
                f"{tasks_text}\n\n"
                "Which ONE task should I do next and why? "
                "Answer in one short paragraph."
            ),
            "stream": False,
            "keep_alive": "3m"
        }

        try:
            r = requests.post(url, json=payload, timeout=120)
            r.raise_for_status()
            data = r.json()
            return data.get("response", "No response from Ollama.")
        except Exception as e:
            return f"Error while calling Ollama: {e}"