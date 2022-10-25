from vacancy import Vacancy
import vacancy_info

lang = ["1C", 'C%23', "Kotlin", "Java", "Python"]
# url # = %23

vacancies_list = []

for i in range(vacancy_info.get_vacansies_count):
    v = Vacancy(
        v.get_vacacy_title(),
        v.get_vacancy_salary(),
        v.get_vacancy_author(),
        v.get_vacancy_link()
    )
    vacancies_list.append()

print(vacancies_list[3])