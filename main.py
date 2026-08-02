from client import TodoClient


def main():
    client = TodoClient()

    while True:
        print("\n===== REST Клиент =====")
        print("1. Получить все задачи")
        print("2. Найти задачу по ID")
        print("3. Показать выполненные")
        print("4. Показать невыполненные")
        print("5. Найти задачи пользователя")
        print("6. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            client.show_all()

        elif choice == "2":
            try:
                task_id = int(input("Введите ID задачи: "))
                client.find_by_id(task_id)
            except ValueError:
                print("Введите число.")

        elif choice == "3":
            client.show_completed_task()

        elif choice == "4":
            client.show_uncompleted_task()

        elif choice == "5":
            try:
                user_id = int(input("Введите ID пользователя: "))
                client.show_user_tasks(user_id)
            except ValueError:
                print("Введите число.")

        elif choice == "6":
            print("Закрытие программы.")
            break

        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()