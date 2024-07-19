import json
from abc import ABC, abstractmethod
# from src.hh import HeadHunterAPI
from src.vacancy import Vacancy
import os
from config import ABSPATH


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

    def __init__(self):
        """ Конструктор для JSONSaver """
        self.path = ABSPATH

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
            new_data = {'id': vacancy.id, 'name': vacancy.name, 'url': vacancy.url,'salary': vacancy.salary, 'experience': vacancy.experience, 'area': vacancy.area}
            data.append(new_data)

            # Записываем новые данные в файл
            with open(self.path, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f'Возникла ошибка {type(e)}')

    def delete_vacancy(self, id: int):
        """ Удаляет данные по вакансии если переданный id совпадает с id вакансии """
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)

            ids = [int(el['id']) for el in data]

            new_data = [el for el in data if int(el['id']) != id]

            if id in ids:
                print(f'Вакансия {id} удалена\n')
            else:
                print(f'Вакансия {id} не найдена в vacancies.json\n')

            with open(self.path, 'w') as file:
                json.dump(new_data, file, ensure_ascii=False, indent=4)



        except json.decoder.JSONDecodeError:
            print('Файл vacancies.json не содержит ни одной вакансии\n')
        # new_data = []
        # vacancy_values = [el for el in vacancy.__dict__.values()]
        #
        # for line in data:
        #     line_values = [el for el in line.values()]
        #     if not line_values == vacancy_values:
        #         new_data.append(line)
        #     else:
        #         continue



    def get_info_by_criterion(self, criterion: str):
        with open(self.path, 'r') as file:
            data = json.load(file)
            data_by_criterion = []
            try:
                for line in data:
                    data_by_criterion.append(line[criterion.lower()])
                return data_by_criterion
            except KeyError:
                return 'Такого критерия не существует'



