from DB.database import init_db
from Controllers.main_controller import MainController

def print_menu():
    print("\n--- TO DO MENU ---")
    print("1) Add task")
    print("2) Show all tasks")
    print("3) Update task status (Open/Done)")
    print("4) Delete task")
    print("5) Ask AI for suggestion")
    print("0) Exit")

def print_tasks_table(tasks):
    print("\nID | Title                | Priority | Status")
    print("------------------------------------------------")
    for t in tasks:
        print(f"{t.id:<2} | {t.title[:20]:<20} | {t.priority:<8} | {t.status}")

def main():
    init_db()
    controller = MainController()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            description = input("Task description: ").strip()
            priority = input("Priority (Low/Medium/High): ").strip().capitalize()

            new_id = controller.add_task(title, description, priority)
            print(f"Task added with id {new_id}")

        elif choice == "2":
            tasks = controller.list_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print_tasks_table(tasks)

        elif choice == "3":
            task_id_text = input("Task id to update: ").strip()
            if not task_id_text.isdigit():
                print("Invalid id (must be a number).")
                continue

            task_id = int(task_id_text)

            tasks = controller.list_tasks()
            if not any(t.id == task_id for t in tasks):
                print("Task id not found")
                continue

            new_status = input("New status (Open/Done): ").strip().capitalize()
            if new_status not in ("Open", "Done"):
                print("Invalid status (must be Open or Done).")
                continue

            ok = controller.change_task_status(int(task_id_text), new_status)
            print("Task updated" if ok else "Task id not found")

        elif choice == "4":
            task_id_text = input("Task id to delete: ").strip()
            if not task_id_text.isdigit():
                print("Invalid id (must be a number).")
                continue

            ok = controller.remove_task(int(task_id_text))
            print("Task deleted" if ok else "Task id not found")

        elif choice == "5":
            print("Asking AI for suggestion...")
            suggestion = controller.get_ai_suggestion()
            print("\n--- AI Suggestion ---")
            print(suggestion)
            print("---------------------")

        elif choice == "0":
            print("Goodbye")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()