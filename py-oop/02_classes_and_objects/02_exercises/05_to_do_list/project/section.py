from project.task import Task

class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def task_exists(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:

                return True

        return False

    def add_task(self, new_task: Task):
        if self.task_exists(new_task.name):

            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:

                task.completed = True

            return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0

        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                count += 1

        return f"Cleared {count} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        result += '\n'.join(task.details() for task in self.tasks)

        return result


