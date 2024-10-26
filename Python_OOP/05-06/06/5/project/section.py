class Section:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks = []

    def add_task(self, new_task: str):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task} is added to the section'

    def complete_task(self, task_name: str):
        pass

    def clean_section(self):
        pass

    def view_section(self):
        pass


