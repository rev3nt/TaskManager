import json
from json import JSONDecodeError


class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, description: str):
        description = description.strip()

        if description:
            self.task_list.append({"description": description, "completed": False})

            print(f'Таск {description} успешно добавлен')
        else:
            print("Добавьте описания таска")

    def complete_task(self, index: int):
        if len(self.task_list) == 0:
            print('Список задач пуст')

            return

        try:
            if self.task_list[index]["completed"]:
                print(f'Таск {self.task_list[index]["description"]} уже помечен, как выполненнный')
            else:
                self.task_list[index]["completed"] = True

                print(f'Статус таска {self.task_list[index]["description"]} изменен')
        except IndexError:
            print("Таска под таким индексом нет")

    def remove_task(self, index: int):
        if len(self.task_list) == 0:
            print('Список задач пуст')

            return

        try:
            del self.task_list[index]

            print(f'Таск под индексом {index} успешно удален')
        except IndexError:
            print("Таска под таким индексом нет")

    def save_to_json(self, file_name: str):
        if len(self.task_list) == 0:
            print('Список задач пуст')

            return

        try:
            with open(file_name, "w", encoding='utf-8') as file:
                json.dump(self.task_list, file, indent=4, ensure_ascii=False)

            print('Таски успешно сохранены в файл')
        except JSONDecodeError:
            print('Подана некорректная JSON строка')

    def load_from_json(self, file_name: str):
        try:
            with open (file_name, "r") as file:
                self.task_list = json.load(file)

            print('Таски загружены из файла')
        except FileNotFoundError:
            print("JSON файл не был найден")
        except JSONDecodeError:
            print("Ошибка декодирвоания JSON(файл поврежден, пуст, либо в нем есть ошибка)")