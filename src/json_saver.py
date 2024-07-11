import json
from abc import ABC, abstractmethod
# from src.hh import HeadHunterAPI
from src.vacancy import Vacancy
import os


class JSON(ABC):
    """ Абстрактный класс для работы с json файлами """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass


class JSONSaver(JSON):
    """ Класс для сохранения данных в json файл """

    def __init__(self, filename):
        """ Конструктор для JSONSaver """
        self.filename = filename
        self.path = os.path.abspath(f"../data/{self.filename}")

    def add_vacancy(self, vacancy: Vacancy):
        """ Добавляет данные по вакансии в self.filename """
        try:
            # Проверяем существует ли файл
            if os.path.exists(self.path):
                with open(self.path, 'r', encoding='utf-8') as file:
                    try:
                        data = json.load(file)
                        if not isinstance(data, list):
                            print(f'Ошибка: ожидался список, но в {self.filename} другой формат')
                            return
                    except json.JSONDecodeError:
                        # Если файл пустой или хранится не cписком в json создаем пустой список
                        data = []
            else:
                data = []
            new_data = {'Профессия': vacancy.name, 'Ссылка': vacancy.url,'Зарплата': vacancy.salary, 'Опыт': vacancy.experience, 'Город': vacancy.city}
            data.append(new_data)

            # Записываем новые данные в файл
            with open(self.path, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f'Возникла ошибка {type(e)}')

    def delete_vacancy(self, vacancy: Vacancy):
        """ Удаляет данные по вакансии из self.filename """
        with open(self.filename, 'r') as file:
            data = json.load(file)

        new_data = []
        vacancy_values = [el for el in vacancy.__dict__.values()]

        for line in data:
            line_values = [el for el in line.values()]
            if not line_values == vacancy_values:
                new_data.append(line)
            else:
                continue

        with open(self.filename, 'w') as file:
            json.dump(new_data, file, ensure_ascii=False, indent=4)


    def get_info_by_criterion(self, criterion: str):
        with open(self.path, 'r') as file:
            data = json.load(file)
            data_by_criterion = []
            try:
                for line in data:
                    data_by_criterion.append(line[criterion.title()])
                return data_by_criterion
            except KeyError:
                return 'Такого критерия не существует'



