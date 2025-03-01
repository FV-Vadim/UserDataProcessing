import pytest

from src.task import Task
from src.user import User


@pytest.fixture
def first_user():
    return User(
        username="Ivan",
        email="ivan@email.com",
        first_name="Ivan",
        last_name="Ivanov",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата"),
        ],
    )


@pytest.fixture
def second_user():
    return User(
        username="John",
        email="john@email.com",
        first_name="John",
        last_name="Doe",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата"),
            Task("Купить лук", "Купить лук для салата"),
        ],
    )


@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="01.03.2025")
