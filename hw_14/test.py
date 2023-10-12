import os

import pytest

from company import Company, LevelException
from employee import Employee


@pytest.fixture
def name():
    name = ['Иван Иванович Иванов', '123 Иванов', 'Иван иванович Иванов', 1234]
    return name


@pytest.fixture()
def level():
    level = [1, 9, '-3']
    return level


@pytest.fixture()
def id_():
    id_ = ['000123', '012', 'fr1105']
    return id_


def test_name_type(name, level, id_):
    with pytest.raises(TypeError, match=r'ФИО должно состоять только '
                                        r'из букв и начинаться с заглавной буквы'):
        Employee(name[3], level[0], id_[0])


def test_name_title(name, level, id_):
    with pytest.raises(ValueError, match=r'ФИО должно состоять только '
                                         r'из букв и начинаться с заглавной буквы'):
        Employee(name[2], level[0], id_[0])


def test_name_number(name, level, id_):
    with pytest.raises(ValueError, match=r'ФИО должно состоять только '
                                         r'из букв и начинаться с заглавной буквы'):
        Employee(name[1], level[0], id_[0])


def test_level_1(name, level, id_):
    with pytest.raises(ValueError, match=r'Значение должно быть целым числом от 1 до 7'):
        Employee(name[0], level[1], id_[0])


def test_level_2(name, level, id_):
    with pytest.raises(ValueError, match=r'Значение должно быть целым числом от 1 до 7'):
        Employee(name[0], level[2], id_[0])


def test_id_1(name, level, id_):
    with pytest.raises(ValueError, match=r'ID должен состоять из 6 цифр'):
        Employee(name[0], level[0], id_[1])


def test_id_2(name, level, id_):
    with pytest.raises(ValueError, match=r'ID должен состоять из 6 цифр'):
        Employee(name[0], level[0], id_[2])


def test_eq_1(name, level, id_):
    employee_1 = Employee(name[0], level[0], id_[0])
    employee_2 = Employee(name[0], level[0], id_[0])
    assert employee_1 == employee_2


def test_eq_2(name, level, id_):
    employee = Employee(name[0], level[0], id_[0])
    with pytest.raises(ValueError, match=r'Недопустимая операция'):
        employee.__eq__(45)


@pytest.fixture
def set_company(request):
    company = Company('test')

    def teardown():
        if os.path.exists('test.json'):
            os.remove('test.json')

    request.addfinalizer(teardown)

    return company


def test_level_access_1(set_company):
    employee = Employee('Иван Сидоров', 1, '123124')
    name = 'Иван Иванов'
    new_id = '134135'
    lvl = 5
    with pytest.raises(LevelException, match=r'Ошибка уровня доступа'):
        set_company.get_job(employee, name, lvl, new_id)


def test_level_access_2(set_company):
    name = 'Иван Иванов'
    new_id = '134135'
    lvl = 5
    employee = set_company.log(name, new_id)
    with pytest.raises(LevelException, match=r'Ошибка доступа'):
        set_company.get_job(employee, name, lvl, new_id)


if __name__ == '__main__':
    pytest.main(['-v'])
