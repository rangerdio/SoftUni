from project import task
from project.task import Task


class Section:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks: list = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str) -> str:
        if task_name in self.tasks:
            task_name.completed = True
            return f'Completed task {task_name}'
        else:
            return f'Task {task_name} is not found in the section {self.name}'

    def clean_section(self) -> str:
        amount_removed_tasks = 0
        for current_task in self.tasks:
            if current_task.completed:
                self.tasks.remove(current_task)
                amount_removed_tasks += 1
        return f'Cleared {amount_removed_tasks} tasks.'

    def view_section(self) -> str:
        result = ''
        result += f'Section {self.name}:'
        for current_task in self.tasks:
            result += f'\n{current_task.details()}'
        return result

