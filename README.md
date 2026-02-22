**AI-Powered To-Do List**
A task management application built with Python, demonstrating Object-Oriented Programming (OOP) principles and the MVC (Model-View-Controller) design pattern.

**System Architecture**
  **Model:** Defines the Task entity with encapsulated attributes and dunder methods for data representation.

  **View:** A command-line interface (CLI) that handles user interaction through a REPL loop.

  **Controller:** Coordinates logic between the UI and the database, and manages AI integration.

  **Database:** Provides persistent storage using SQLite with full CRUD support.

**Features**
  **Task Management:** Create, view, update, and delete tasks.

  **Persistent Storage:** Data is saved locally in a SQL database.

  **AI Suggestions:** Integrates with a local Ollama server (Llama 3.1) to analyze tasks and suggest the next best action.

**Setup & Execution**
  **Install dependencies:** pip install requests.

  **Run the app:** python main.py.

  **(Optional) Ensure Ollama is running locally for AI features.**
