from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def show_info(self):
        status = "Виконано" if self.completed else "Не виконано"
        print(f"Назва: {self.title}")
        print(f"Опис: {self.description}")
        print(f"Дедлайн: {self.deadline}")
        print(f"Стан: {status}")
        print("-" * 30)


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()

    def show_all_tasks(self):
        if not self.tasks:
            print("Список завдань порожній")
        for task in self.tasks:
            task.show_info()

manager = TaskManager()

task1 = Task("Домашка", "Зробити математику", "2026-04-30")
task2 = Task("Проєкт", "Зробити Python проєкт", "2026-05-05")

manager.add_task(task1)
manager.add_task(task2)

# Позначаємо одне як виконане
manager.mark_task_completed("Домашка")
manager.remove_task("Проєкт")
manager.show_all_tasks()