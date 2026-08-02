import requests

from config import BASE_URL


class TodoClient:
    def __init__(self):
        self.todos = []
        self.load_todos()

    def load_todos(self) -> None:
        """Загружает список задач из REST API"""
        self.session = requests.Session()
        response = self.session.get(BASE_URL, timeout=5)
        try:
            
            response.raise_for_status()
            self.todos = response.json()
            print("Данные успешно загружены.")
        except requests.exceptions.RequestException as error:
            print("Ошибка при загрузке данных:", error)

    def print_task(self, task: dict) -> None:
        """Совершает вывод задачи"""
        status = "Yes" if task["completed"] else "No"

        print(f"\nID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Completed: {status}")
        print("-" * 40)

    def show_all(self) -> None:
        for task in self.todos:
            self.print_task(task)

    def find_by_id(self, task_id: int) -> None:
        for task in self.todos:
            if task["id"] == task_id:
                self.print_task(task)
                return
        print("Задача не найдена.")

    def show_completed_task(self) -> None:
        for task in self.todos:
            if task["completed"]:
                self.print_task(task)

    def show_uncompleted_task(self) -> None:
        for task in self.todos:
            if not task["completed"]:
                self.print_task(task)

    def show_user_tasks(self, user_id: int) -> None:
        """Вывод задач пользователя"""
        found = False

        for task in self.todos:
            if task["userId"] == user_id:
                self.print_task(task)
                found = True

        if not found:
            print("У пользователя нет задач.")
