import psycopg2
import os


class DBManager:

    user = os.environ.get('USER')
    password = os.environ.get('PASSWORD')
    database = os.environ.get('DATABASE')

    def get_companies_and_vacancies_count(self) -> list:
        '''
        Получает список всех компаний и количество вакансий у каждой компании.
        :return:
        '''
        with psycopg2.connect(host='localhost', database=self.database, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT employers.employer_name, COUNT(vacancy.*) FROM employers
                                INNER JOIN vacancy USING(employer_id) GROUP BY employers.employer_name""")
                rows = cur.fetchall()
        return rows

    def get_all_vacancies(self) -> list:
        '''
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        :return:
        '''
        with psycopg2.connect(host='localhost', database=self.database, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT employers.employer_name, vacancy_name, salary_from, salary_to, url
                                FROM vacancy INNER JOIN employers USING(employer_id)""")
                rows = cur.fetchall()
        return rows


    def get_avg_salary(self) -> list:
        """
        Получает среднюю зарплату по вакансиям.
        :return:
        """
        with psycopg2.connect(host='localhost', database=self.database, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT AVG(salary_from), AVG(salary_to) FROM vacancy')
                rows = cur.fetchall()
        return rows

    def get_vacancies_with_higher_salary(self) -> list:
        '''
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        :return:
        '''
        with psycopg2.connect(host='localhost', database=self.database, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM vacancy\
                 WHERE (SELECT AVG(salary_from+salary_to) FROM vacancy)< salary_from+salary_to")
                rows = cur.fetchall()
        return rows
    def get_vacancies_with_keyword(self, name) -> list:
        '''
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.
        :return:
        '''
        with psycopg2.connect(host='localhost', database=self.database, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancy WHERE vacancy_name LIKE '%{name}%'")
                rows = cur.fetchall()
        return rows

