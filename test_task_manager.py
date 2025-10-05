from task_manager import TaskManager
import pytest


TASK_LIST = [
    ([
        {"description": "Task 1"},
    ]),
    ([
        {"description": ""},
    ]),
    ([])
]

FILE_NAME = 'saved_tasks.json'


@pytest.fixture
def json_file_cleaner():
    yield

    with open(FILE_NAME, 'w') as file:
        pass


@pytest.fixture
def task_manager_setup():
    return TaskManager()


@pytest.mark.parametrize("tasks_list", TASK_LIST)
def test_add_and_complete_task(task_manager_setup, tasks_list):
    tm = task_manager_setup

    for task in tasks_list:
        tm.add_task(task['description'])

    initial_task_count = len(tm.__dict__['task_list'])

    assert len(tm.__dict__['task_list']) == initial_task_count

    if initial_task_count > 0:
        tm.complete_task(0)

        assert tm.__dict__['task_list'][0]['completed']
    else:
        tm.complete_task(0)
        assert (len(tm.__dict__['task_list'])) == initial_task_count


@pytest.mark.parametrize("tasks_list", TASK_LIST)
def test_delete_task(task_manager_setup, tasks_list):
    tm = task_manager_setup

    for task in tasks_list:
        tm.add_task(task['description'])

    initial_task_count = len(tm.__dict__['task_list'])

    if initial_task_count > 0:
        tm.remove_task(0)

        assert len(tm.__dict__['task_list']) == initial_task_count - 1
    else:
        tm.remove_task(0)
        assert (len(tm.__dict__['task_list'])) == initial_task_count


@pytest.mark.parametrize("tasks_list", TASK_LIST)
def test_save_and_load_task(task_manager_setup, json_file_cleaner, tasks_list):
    tm_to_save = task_manager_setup

    tm_to_load = TaskManager()

    for task in tasks_list:
        tm_to_save.add_task(task['description'])

    print(tm_to_load.__dict__['task_list'])

    tm_to_save.save_to_json(FILE_NAME)

    tm_to_load.load_from_json(FILE_NAME)

    assert tm_to_save.__dict__['task_list'] == tm_to_load.__dict__['task_list']
