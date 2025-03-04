class Task:
    def __init__(self, name):
        self.name = name
        self.is_completed = False

    def complete(self):
        self.is_completed = True


class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.taks.append(task)

    def 