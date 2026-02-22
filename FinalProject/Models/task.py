class Task:
    def __init__(self, task_id, title, description, priority, status):
        self._id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    @property
    def id(self):
        return self._id

    def __repr__(self):
        return (
            f"Task(Task ID={self.id}, title='{self.title}', "
            f"priority='{self.priority}', status='{self.status}')"
        )