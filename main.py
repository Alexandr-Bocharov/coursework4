import requests
import json
from src.json_saver import JSONSaver
from src.vacancy import Vacancy
from src.hh import HeadHunterAPI
from src.utils import (search_query,
                       clear_json,
                       # get_vacancies_by_salary,
                       # filter_vacancies,
                       sort_vacancies,
                       get_top_vacancies,
                       print_vacancies)

hh1 = HeadHunterAPI()
hh1_vacancies = hh1.get_vacancies('python')
vacancies_list = Vacancy.cast_to_object_list(hh1_vacancies)

json_saver = JSONSaver('vacancies.json')


def user_interaction():
    platforms = ["HeadHunter"]
    keywords_for_search = input("Введите поисковый запрос: ").split()
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))


    filtered_vacancies = search_query(keywords_for_search)

    top_vacancies = get_top_vacancies(filtered_vacancies, top_n)
    sorted_vacancies = sort_vacancies(top_vacancies)
    print_vacancies(sorted_vacancies)


if __name__ == '__main__':
    user_interaction()






