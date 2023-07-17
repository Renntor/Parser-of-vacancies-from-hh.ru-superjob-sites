from src.utils import employees_list_processing, vacancy_list_processing, adding_date_in_sql
from src.Employers import Employers
from src.DBManager import DBManager
import psycopg2


if __name__ == '__main__':
    employers = Employers()
    employees_list = employees_list_processing(employers.get_info_employers())
    vacancy_list = vacancy_list_processing(employers.get_info_vacancies())

    user = input('Привет! Напиши данные для входа в базу данных \nИмя пользователя: ')
    password = input('Пароль: ')
    database = input('Название базы данных: ')
    try:
        dbmanager = DBManager(database, user, password)
        adding_date_in_sql(database, user, password, employees_list, vacancy_list)
    except psycopg2.OperationalError as e:
        exit(f'{e}Неверные данные!')

    while True:
        user_input = input('Напиши номер данных, которые необходимо вывести?\n\
Все компании и количество вакансий - 1\n\
Все вакансии с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию - 2\n\
Среднюю зарплату по вакансиям - 3\n\
Все вакансии, у которых зарплата выше средней по всем вакансиям - 4\n\
Найти вакансии с определенным именем - 5\n\
Закончить работу - Стоп\n')

        if user_input == '1':
            for row in dbmanager.get_companies_and_vacancies_count():
                print(row)
        elif user_input == '2':
            for row in dbmanager.get_all_vacancies():
                print(row)
        elif user_input == '3':
            for row in dbmanager.get_avg_salary():
                print(f'от {round(row[0])} до {round(row[1])}')
        elif user_input == '4':
            for row in dbmanager.get_vacancies_with_higher_salary():
                print(row)
        elif user_input == '5':
            job_name = input('Название вакансии: ')
            for row in dbmanager.get_vacancies_with_keyword(job_name):
                print(row)
        elif user_input.lower() == 'стоп':
            break
        else:
            print('Неверные данные!')
