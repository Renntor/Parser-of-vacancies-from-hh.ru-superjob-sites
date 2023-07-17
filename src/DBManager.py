import psycopg2
import os


class DBManager:

    def __init__(self, database: str, user: str, password: str):
        self.database = database
        self.user = user
        self.password = password
        self.conn = psycopg2.connect(host='localhost', database=self.database, user=self.user, password=self.password)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self) -> list:
        '''
        Получает список всех компаний и количество вакансий у каждой компании.
        :return:
        '''
        self.cur.execute("""SELECT employers.employer_name, COUNT(vacancy.vacancy_id) AS count_vacancy FROM employers
                       INNER JOIN vacancy USING(employer_id) GROUP BY employers.employer_name""")
        rows = self.cur.fetchall()
        return rows

    def get_all_vacancies(self) -> list:
        '''
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        :return:
        '''
        self.cur.execute("""SELECT employers.employer_name, vacancy_name, salary_from, salary_to, url
                        FROM vacancy INNER JOIN employers USING(employer_id)""")
        rows = self.cur.fetchall()
        return rows


    def get_avg_salary(self) -> list:
        """
        Получает среднюю зарплату по вакансиям.
        :return:
        """
        self.cur.execute('SELECT AVG(salary_from), AVG(salary_to) FROM vacancy')
        rows = self.cur.fetchall()
        return rows

    def get_vacancies_with_higher_salary(self) -> list:
        '''
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        :return:
        '''
        self.cur.execute("SELECT * FROM vacancy\
         WHERE (SELECT AVG(salary_from+salary_to) FROM vacancy)< salary_from+salary_to")
        rows = self.cur.fetchall()
        return

    def get_vacancies_with_keyword(self, name) -> list:
        '''
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.
        :return:
        '''
        self.cur.execute(f"SELECT * FROM vacancy WHERE vacancy_name LIKE '%{name}%'")
        rows = self.cur.fetchall()
        return rows

