from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import requests
from src.json_saver import JSONSaver
import json
from src.vacancy import Vacancy
import os


class Api(ABC):
    """ Абстрактный класс для работы с API """

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(Api):
    """ Класс для работы с API HeadHunter """

    def __init__(self):
        """ Конструктор для HeadHunterAPI """
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 10}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 1:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 10:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies += vacancies
            self.params['page'] += 1
        return self.vacancies



    