

def test_vacancy_init(vacancy1):
    assert vacancy1.salary == {'from': 42435, 'to': 0, 'currency': 'KZT', 'gross': 0}
    assert vacancy1.experience == 'нет опыта'


def test_vacancy_eq_lt(vacancy1, vacancy2):
    assert vacancy1 < vacancy2
    assert vacancy2 >= vacancy1
    assert not vacancy1 == vacancy2
    assert vacancy1 < 100000
    assert vacancy1 >= 5000


def test_vacancy_get_salary_str(vacancy2, vacancy3):
    assert vacancy3.get_salary_str() == 'Зарплата не указана'
    assert vacancy2.get_salary_str() == 'От 54054 до 81081'


def test_vacancy_get_salary_avg(vacancy2, vacancy3):
    assert vacancy2.get_salary_for_sort() == 81081
    assert vacancy3.get_salary_for_sort() == 0


def test_vacancy_get_salary(vacancy1):
    assert vacancy1.get_salary() == 42435

