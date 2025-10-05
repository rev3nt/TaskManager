from task_manager import TaskManager
import pytest

TASK_LIST = [
        ([
        {"description": "Task 1"},
        {"description": "Task 2"},
        {"description": "Task 3"},
        {"description": "Task 4"}
        ]),
        ([
            {"description": ""},
            {"description": "    "},
            {"description": "Only this should be in list"}
        ]),
        ([])
    ]

FILE_NAME = 'saved_tasks.json'

@pytest.fixture
def json_file_cleaner():
    yield

    with open(FILE_NAME, 'w') as file:
        pass


@pytest.mark.parametrize("tasks_list", TASK_LIST)
def test_add_and_complete_task(tasks_list):
    tm = TaskManager()

    for task in tasks_list:
       tm.add_task(task['description'])

    initial_task_count = len(tm.__dict__['task_list'])

    assert len(tm.__dict__['task_list']) == initial_task_count

    if initial_task_count > 0:
        tm.complete_task(0)

        assert tm.__dict__['task_list'][0]['completed'] == True
    else:
        tm.complete_task(0)
        assert (len(tm.__dict__['task_list'])) == initial_task_count


@pytest.mark.parametrize("tasks_list", TASK_LIST)
def test_delete_task(tasks_list):
    tm = TaskManager()

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
def test_save_and_load_task(json_file_cleaner, tasks_list):
    tm_to_save = TaskManager()

    tm_to_load = TaskManager()

    for task in tasks_list:
        tm_to_save.add_task(task['description'])

    tm_to_save.save_to_json(FILE_NAME)

    tm_to_load.load_from_json(FILE_NAME)

    assert tm_to_save.__dict__['task_list'] == tm_to_load.__dict__['task_list']