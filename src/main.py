from src.Employers import Employers
from src.Saver import Saver


def main():
    employers = Employers()
    saver = Saver()

    info_empl = employers.get_info_employers()
    info_vac = employers.get_info_vacancies()
    saver.save_employers(info_empl)
    saver.save_vacancy(info_vac)


if __name__ == '__main__':
    main()
