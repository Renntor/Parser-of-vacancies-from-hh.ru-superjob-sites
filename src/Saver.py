import psycopg2
import os


class Saver:
    user = os.environ.get('USER')
    password = os.environ.get('PASSWORD')
    database = os.environ.get('DATABASE')

    def save_employers(self, employers: list) -> None:
        """
        Сохранение работодателей в БД
        :param employers: список с данными о работодателях
        :return: None
        """
        with psycopg2.connect(host='localhost', database=self.database, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                for i in employers:
                    cur.execute("INSERT INTO employers VALUES (%s, %s, %s, %s)",
                                (int(i['id']), i['name'], i['description'], i['site_url']))

    def save_vacancy(self, vacancy: list) -> None:
        """
        Сохранение вакансий в БД
        :param vacancy: список с данными о вакансиях
        :return: None
        """
        with psycopg2.connect(host='localhost', database=self.database, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                for i in vacancy:
                    for items in i['items']:
                        # проверка на наличие зарплаты
                        if items['salary'] is not None:
                            salary_from = items['salary']['from']
                            salary_to = items['salary']['to']
                        else:
                            salary_from = None
                            salary_to = None
                        # запись данных по вакансиям в список
                        data_list = [items['employer']['id'], items['name'], items['published_at'],
                                     items['alternate_url'], items['snippet']['requirement'],
                                     items['snippet']['responsibility'], items['experience']['name'],
                                     items['employment']['name'], salary_from, salary_to]
                        cur.execute('INSERT INTO vacancy (employer_id, vacancy_name, published_date,\
                        url, requirement, responsibility, experience, employment, salary_from, salary_to)\
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', data_list)
