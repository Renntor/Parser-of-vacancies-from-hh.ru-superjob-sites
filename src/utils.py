import psycopg2


def employees_list_processing(employers: list) -> list:
    """
    Сохранение работодателей в БД
    :param employers: список работодателей
    :return: список обработанных данных работодателях
    """
    return [(int(i['id']), i['name'], i['description'], i['site_url']) for i in employers]


def vacancy_list_processing(vacancy: list) -> list:
    """
    Сохранение вакансий в БД
    :param vacancy: список вакансий
    :return: список обработанных данных вакансий
    """
    data_list = []
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
            data_list.append([items['employer']['id'], items['name'], items['published_at'],
                         items['alternate_url'], items['snippet']['requirement'],
                         items['snippet']['responsibility'], items['experience']['name'],
                         items['employment']['name'], salary_from, salary_to])
    return data_list


def adding_date_in_sql(database: str, user: str, password: str, list_employees: list, list_vacancy: list) -> None:
    """
    Запись данных в БД
    :param database: имя базы данных
    :param user: логин пользователя базы данных
    :param password: пароль пользователя базы данных
    :param list_employees: список работодателей для записи в БД
    :param list_vacancy: список вакансий для записи в БД
    :return: None
    """
    with psycopg2.connect(host='localhost', database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            for i in list_employees:
                cur.execute("INSERT INTO employers VALUES (%s, %s, %s, %s)", i)
            for i in list_vacancy:
                cur.execute('INSERT INTO vacancy (employer_id, vacancy_name, published_date,\
                url, requirement, responsibility, experience, employment, salary_from, salary_to)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', i)

