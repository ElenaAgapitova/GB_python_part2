from company import Company


if __name__ == '__main__':
    uts = Company('uts')
    print(*uts.employees, sep='\n')
    print()
    employer = uts.log('Майя Геннадьевна Горбачева', '370241')
    new_employer_1 = uts.get_job(employer, 'Иван Иванович Иванов', "1", '123123')
    print(*uts.employees, sep='\n')
    new_employer_2 = uts.get_job(employer, 'Владимир Владимирович Путин', 7, '777777')


