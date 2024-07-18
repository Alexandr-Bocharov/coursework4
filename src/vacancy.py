from functools import total_ordering
from abc import ABC, abstractmethod
from src.currency import CurrencyFromRUR


class AbstractVacancy(ABC):
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass


@total_ordering
class Vacancy:


    @classmethod
    def cast_to_object_list(cls, json_vacancies):
        """ Из элементов json_vacancies создает объекты класса Vacancy и возвращает список экземпляров Vacancy """
        new_list = []
        for line in json_vacancies:
            if line:
                salary = line['salary']
                try:
                    vacancy = line['name']
                except TypeError:
                    vacancy = None
                try:
                    experience = line['experience']
                except TypeError:
                    experience = None
                try:
                    city = line['area']
                except TypeError:
                    city = None

                new_list.append(cls(vacancy, line['url'], salary, experience, city))
        return new_list

    def __init__(self, name: str, url: str, salary: None | dict, experience: dict, area: dict, currency=CurrencyFromRUR()):
        """ Конструктор для Vacancy """
        self.name = name
        self.url = url
        if salary:
            for k, v in salary.items():
                if not v:
                    salary[k] = 0
            if salary['currency'] == 'USD':
                salary['from'] = round(salary['from'] / currency.USD)
                salary['to'] = round(salary['to'] / currency.USD)
            if salary['currency'] == 'BUR':
                salary['from'] = round(salary['from'] / currency.BUR)
                salary['to'] = round(salary['to'] / currency.BUR)
            if salary['currency'] == 'KZT':
                salary['from'] = round(salary['from'] / currency.KZT)
                salary['to'] = round(salary['to'] / currency.KZT)
            if salary['currency'] == 'EUR':
                salary['from'] = round(salary['from'] / currency.EUR)
                salary['to'] = round(salary['to'] / currency.EUR)
            salary['currency'] = 'RUR'
            self.salary = salary
        else:
            self.salary = 0
        self.experience = experience
        self.area = area

    def __repr__(self):
        """ Для отладки и удобного представления экземпляра для пользователя """
        return f'{self.name} /// Ссылка: {self.url} /// з/п: {self.get_salary_str()} /// Опыт: {self.experience} /// Город: {self.area['name']}'

    def __eq__(self, other):
        """ Сравнивает по get_salary_for_sort """
        if isinstance(other, Vacancy):
            return self.get_salary_for_sort() == other.get_salary_for_sort()
        if isinstance(other, int):
            return self.get_salary_for_sort() == other

    def __lt__(self, other):
        """ Сравнивает по get_salary_for_sort """
        if isinstance(other, Vacancy):
            return self.get_salary_for_sort() < other.get_salary_for_sort()
        if isinstance(other, int):
            return self.get_salary_for_sort() < other

    def get_salary_str(self) -> str:
        """ Возвращает простое строковое представление зарплаты для последующего использования в __repr__ """
        if self.salary:
            if self.salary['from'] and self.salary['to']:
                return f'От {self.salary["from"]} до {self.salary["to"]}'
            if self.salary['from']:
                return f'От {self.salary["from"]}'
            if self.salary['to']:
                return f'До {self.salary["to"]}'
        return 'Зарплата не указана'

    def get_salary_for_sort(self) -> int:
        """ Возвращает числовое значение для дальнейшей сортировки вакансий по зарплате """
        if self.salary:
            if self.salary['from']:
                return self.salary['from']
            if self.salary['to']:
                return self.salary['to']
        return self.salary

# vacancies_list.sort(reverse=True, key=lambda x: (x['Зарплата'],) if not x['Зарплата'] else (x['Зарплата']['from'], x['Зарплата']['to']))
    def get_salary(self) -> int:
        if self.salary:
            return self.salary['from']



