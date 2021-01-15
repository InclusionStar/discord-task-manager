class TaskHandler():
    def __init__(self, tasks=[]):
        self.tasks = tasks

    def add(self):
        pass

    def delete(self):
        pass

    def clear_all(self):
        pass

    def show_info(self):
        pass


class Task():
    def __init__(self, task_name, sub_tasks, date):
        self.task_name = task_name
        self.sub_tasks = sub_tasks
        self.date = date
