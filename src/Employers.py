import ujson
import httpx


class Employers:

    # список работодателей
    employers_id = ['1740', '1122462', '1057', '3529', '1805417', '15478', '3388', '80', '3749373', '733']

    def get_info_employers(self) -> list:
        """
        Выводит список с описанием работодателей
        :return: list
        """
        info = []
        for i in self.employers_id:
            hh_request = httpx.get('https://api.hh.ru/employers/' + i)
            date_hh = hh_request.content.decode()
            uj_hh = ujson.loads(date_hh)
            info.append(uj_hh)
        return info

    def get_info_vacancies(self) -> list:
        """
        Выводит список с работ от работодателей
        :return: list
        """
        info = []
        for i in self.employers_id:
            hh_job = httpx.get('https://api.hh.ru/vacancies', params={'employer_id': i, 'per_page': 100})
            job_hh = hh_job.content.decode()
            job_json = ujson.loads(job_hh)
            info.append(job_json)
        return info

