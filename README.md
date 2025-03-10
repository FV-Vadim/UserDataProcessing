# UserDataProcessing

Этот проект представляет собой систему для обработки данных пользователей и их задач. Он включает в себя создание объектов пользователей и задач, чтение данных из JSON-файла и их обработку.

## Структура проекта

- `src/`: Основной код проекта.
  - `task.py`: Модуль для работы с задачами.
  - `user.py`: Модуль для работы с пользователями.
  - `utils.py`: Вспомогательные функции для чтения JSON и создания объектов.
- `tests/`: Тесты для проверки функциональности.
- `data/`: Данные в формате JSON.
- `main.py`: Основной скрипт для запуска программы.

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-репозиторий/UserDataProcessing.git
   cd UserDataProcessing
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Запустите основной скрипт:
   ```bash
   python main.py
   ```

## Использование

### Создание задач и пользователей

Пример создания задачи и пользователя:
```
task = Task("Купить огурцы", 'Купить огурцы для салата')
user = User("Ivan", "ivan@email.com", "Ivan", 'Ivanov', [task])
```

### Чтение данных из JSON

Для чтения данных из JSON-файла используйте функцию `read_json`:
```
raw_data = read_json('./data/data.json')
users_data = create_objects_from_json(raw_data)
```

### Запуск тестов

Для запуска тестов используйте команду:
```bash
pytest --cov
```

## Описание модулей

### `task.py`

Модуль содержит класс `Task`, который представляет задачу. Задача имеет следующие атрибуты:
- `name`: Название задачи.
- `description`: Описание задачи.
- `status`: Статус задачи (по умолчанию 'Ожидает старта').
- `created_at`: Дата создания задачи (по умолчанию текущая дата).

### `user.py`

Модуль содержит класс `User`, который представляет пользователя. Пользователь имеет следующие атрибуты:
- `username`: Имя пользователя.
- `email`: Электронная почта пользователя.
- `first_name`: Имя пользователя.
- `last_name`: Фамилия пользователя.
- `task_list`: Список задач пользователя.

Класс также содержит классовые переменные:
- `users_count`: Количество созданных пользователей.
- `all_task_count`: Общее количество задач всех пользователей.

### `utils.py`

Модуль содержит вспомогательные функции:
- `read_json(file_path)`: Читает JSON-файл и возвращает данные.
- `create_objects_from_json(raw_data)`: Создает объекты пользователей из данных JSON.

## Тестирование

Тесты находятся в директории `tests/`. Для запуска тестов используйте команду:
```bash
pytest --cov
```

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).

---

