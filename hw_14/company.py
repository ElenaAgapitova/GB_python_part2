import json
import os

from create_json import create_employee
from employee import Employee


class LevelException(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'


class Company:

    def __init__(self, name: str):
        self.name = name
        if os.path.exists(f'{self.name}.json'):
            with open(f'{self.name}.json', 'r', encoding='UTF-8') as file:
                employees_list = json.load(file)
        else:
            employees_list = create_employee(name, 10)
        self.employees = [Employee(name_, lvl, id_)
                          for lvl, person in employees_list.items()
                          for id_, name_ in person.items()]

    def log(self, name: str, employee_id: str):
        for item in self.employees:
            if item.name == name and item.employee_id == employee_id:
                return item
        return False

    def get_job(self, employer: Employee, employee_name: str, employee_level: int | str, employee_id: str):
        if employer:
            if employer.lvl_access > int(employee_level):
                if employee_id not in [employee.employee_id for employee in self.employees]:
                    self.employees.append(Employee(employee_name, int(employee_level), employee_id))
                    self.__save()
            else:
                raise LevelException('Ошибка уровня доступа')
        else:
            raise LevelException('Ошибка доступа')

    def __save(self):
        employees_dict = {}
        for employee in self.employees:
            if employee.lvl_access in employees_dict:
                employees_dict[employee.lvl_access][employee.employee_id] = employee.name
            else:
                employees_dict[employee.lvl_access] = {employee.employee_id: employee.name}
        with open(f'{self.name}.json', 'w', encoding='UTF-8') as file:
            json.dump(employees_dict, file, indent=4, ensure_ascii=False)
