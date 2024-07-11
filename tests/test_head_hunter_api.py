from src.hh import HeadHunterAPI


def test_head_hunter_api_get_vacancies(request1):
    assert len(request1) == 100
    assert type(request1[0]) == dict
    # assert request1[0]['salary'] == {'from': None, 'to': 400, 'currency': 'USD', 'gross': False}
    # print(request1[0])
    # assert request1[0]['name'] == 'Программист Python'







