from src.utils import (search_query,
                       # get_vacancies_by_salary,
                       # filter_vacancies,
                       sort_vacancies,
                       get_top_vacancies,
                       print_vacancies)


def test_search_query(objects_list):
    assert search_query(['москва'])[0]['Зарплата'] == {'from': 800000, 'to': 1000000, 'currency': 'RUR', 'gross': True}
    assert search_query(['москва'])[1]['Ссылка'] == 'https://api.hh.ru/vacancies/103677273?host=hh.ru'


# def test_get_vacancies_by_salary(objects_list):
#     update_list = get_vacancies_by_salary(objects_list, 30000)
#     assert len(update_list) == 3
#     assert update_list[0].salary == {'from': 42435, 'to': 0, 'currency': 'KZT', 'gross': 0}
#     assert update_list[1].name == 'python разработчик'


# def test_filter_vacancies(objects_list):
#     filtered_list = filter_vacancies(objects_list, ['тестировщик'])
#     assert len(filtered_list) == 1
#     assert filtered_list[0].city == 'Москва'


def test_sort_vacancies(objects_list):
    sorted_list = sort_vacancies(objects_list)
    assert sorted_list[3]['Зарплата'] == 0
    assert sorted_list[2]['Зарплата'] == {'from': 2000, 'to': 3000, 'currency': 'BUR', 'gross': False}


def test_get_top_vacancies(objects_list):
    assert len(get_top_vacancies(objects_list, 2)) == 2
    assert len(get_top_vacancies(objects_list, 3)) == 3




