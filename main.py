from src.task import Task
from src.user import User
from src.utils import create_objects_from_json, read_json

if __name__ == "__main__":

    task = Task("Купить огурцы", "Купить огурцы для салата")

    print(task.name)
    print(task.description)
    print(task.status)
    print(task.created_at)

    task_1 = Task("Купить огурцы", "Купить огурцы для салата")
    task_2 = Task("Купить помидоры", "Купить помидоры для салата")
    task_3 = Task("Купить лук", "Купить лук для салата")
    task_4 = Task("Купить перец", "Купить перец для салата")

    user = User(
        "Ivan", "ivan@email.com", "Ivan", "Ivanov", [task_1, task_2, task_3, task_4]
    )

    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.users_count)
    print(User.all_task_count)

    raw_data = read_json("./data/data.json")
    users_data = create_objects_from_json(raw_data)
    print(users_data[0].username)
    print(users_data[0].task_list)
