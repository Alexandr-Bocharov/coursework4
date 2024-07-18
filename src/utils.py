import json
from src.vacancy import Vacancy
import os


def search_query(keywords: list):
    """ Возвращает список вакансий из json файла, отфильтрованных по keywords """
    path = os.path.abspath("../data/vacancies.json")
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    vacancies_objects = Vacancy.cast_to_object_list(data)

    filtered = []
    filter_words_low = [el.lower() for el in keywords]
    for line in vacancies_objects:
        values_for_filter = [line.name, line.url, line.experience['name'], line.area['name']]
        for word in filter_words_low:
            for el in [el.lower() for el in values_for_filter if isinstance(el, str)]:
                if word in el:
                    filtered.append(line)
                    break

    return filtered


def get_vacancies_by_salary(vacancies_list: list[Vacancy], salary_range: int) -> list[Vacancy]:
    """ Возвращает список отфильтрованных вакансий по зарплате """
    filtered_by_salary = []
    for vacancy in vacancies_list:
        if vacancy.get_salary_for_sort() >= salary_range:
            filtered_by_salary.append(vacancy)


    return filtered_by_salary


# def filter_vacancies(vacancies_list: list[Vacancy], filter_words: list) -> list[Vacancy]:
#     """ Возвращает список вакансий, в которых хоть одно слово из keywords есть в аттрибутах вакансии """
#     filtered = []
#     filter_words_low = [el.lower() for el in filter_words]
#     for line in vacancies_list:
#         for word in filter_words_low:
#             for el in [el.lower() for el in line.__dict__.values() if isinstance(el, str)]:
#                 if word in el:
#                     filtered.append(line)
#                     break
#     return filtered


def sort_vacancies(vacancies_list: list[Vacancy]) -> list[Vacancy]:
    """ Возвращает список вакансий, отсортированных по величине зарплаты от большего к меньшему """
    vacancies_list.sort(reverse=True)  # key=lambda x: (x['Зарплата'], ) if not x['Зарплата'] else (x['Зарплата']['from'], x['Зарплата']['to']))
    return vacancies_list


def get_top_vacancies(vacancies_list: list[Vacancy], top_n: int) -> list[Vacancy]:
    """ Возвращает определенное количество вакансий(а именно top_n) """
    return vacancies_list[:top_n]


def print_vacancies(vacancies_list: list[Vacancy]):
    """ Печатает все вакансии переданные в vacancies_list """
    for vacancy in vacancies_list:
        print(vacancy)


def clear_json(filename):
    path = os.path.abspath(f'../data/{filename}')
    with open(path, 'w') as file:
        pass