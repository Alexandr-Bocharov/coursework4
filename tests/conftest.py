import pytest
from src.hh import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


@pytest.fixture
def request1():
    hh1 = HeadHunterAPI()
    requested = hh1.get_vacancies('python')
    return requested


@pytest.fixture
def vacancy1_for_utils():
    return {'Профессия': 'backend developer',
            'Ссылка': 'https://api.hh.ru/hhh',
            'Зарплата': {'from': 230000, 'to': 0, 'currency': 'KZT', 'gross': False},
            'Опыт': 'нет опыта',
            'Город': 'Астана'}


@pytest.fixture
def vacancy2_for_utils():
    return {'Профессия': 'python разработчик',
            'Ссылка': 'https://api.hh.ru/hhhpth',
            'Зарплата': {'from': 2000, 'to': 3000, 'currency': 'BUR', 'gross': False},
            'Опыт': 'от 3 до 6 лет',
            'Город': 'Минск'}


@pytest.fixture
def vacancy3_for_utils():
    return {'Профессия': 'python разработчик',
            'Ссылка': 'https://api.hh.ru/hhhpth',
            'Зарплата': 0,
            'Опыт': 'от 3 до 6 лет',
            'Город': 'Минск'}


@pytest.fixture
def vacancy4_for_utils():
    return {'Профессия': 'QA тестировщик',
            'Ссылка': 'https://api.hh.ru/hhhhfsvsjh',
            'Зарплата': {'from': 230000, 'to': 300000, 'currency': 'RUR', 'gross': False},
            'Опыт': 'нет опыта',
            'Город': 'Москва'}


@pytest.fixture
def objects_list(vacancy1_for_utils, vacancy2_for_utils, vacancy3_for_utils, vacancy4_for_utils):
    return [vacancy1_for_utils, vacancy2_for_utils, vacancy3_for_utils, vacancy4_for_utils]


@pytest.fixture
def json_saver1():
    return JSONSaver('fdah/fvhjsvsh/file.json')


@pytest.fixture
def json_saver2():
    return JSONSaver('vacancies.json')


@pytest.fixture
def vacancy1():
    # return Vacancy('backend developer',
    #                'https://api.hh.ru/hhh',
    #                {'from': 230000, 'to': 0, 'currency': 'KZT', 'gross': False},
    #                'нет опыта',
    #                'Астана')
    return Vacancy('backend developer',
                   'https://api.hh.ru/hhh',
                   {'from': 230000, 'to': 0, 'currency': 'KZT', 'gross': False},
                   'нет опыта',
                   'Астана')


@pytest.fixture
def vacancy2():
    return Vacancy('python разработчик',
                   'https://api.hh.ru/hhhpth',
                   {'from': 2000, 'to': 3000, 'currency': 'BUR', 'gross': False},
                   'от 3 до 6 лет',
                   'Минск')


@pytest.fixture
def vacancy3():
    return Vacancy('python разработчик',
                   'https://api.hh.ru/hhhpth',
                   None,
                   'от 3 до 6 лет',
                   'Минск')


@pytest.fixture
def vacancy4():
    return Vacancy('QA тестировщик',
                   'https://api.hh.ru/hhhhfsvsjh',
                   {'from': 230000, 'to': 300000, 'currency': 'RUR', 'gross': False},
                   'нет опыта',
                   'Москва')