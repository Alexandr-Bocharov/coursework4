import pytest


def test_json_saver_add_vacancy(json_saver1, vacancy1, capsys):
    json_saver1.add_vacancy(vacancy1)
    message = capsys.readouterr()
    assert message.out.strip() == "Возникла ошибка <class 'FileNotFoundError'>"


def test_json_saver_get_info_by_criterion(json_saver1, json_saver2):
    assert json_saver2.get_info_by_criterion('fhjsbvhshs') == 'Такого критерия не существует'
    assert isinstance(json_saver2.get_info_by_criterion('Опыт'), list)
