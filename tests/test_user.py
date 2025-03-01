

def test_user_init(first_user, second_user):
    assert first_user.username == "Ivan"
    assert first_user.email == "ivan@email.com"
    assert len(first_user.task_list) == 2

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_task_count == 5
    assert second_user.all_task_count == 5
