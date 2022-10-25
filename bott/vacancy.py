class Vacancy:
    # vacancy_technology = ""
    vacancy_title = ""
    vacancy_salary = ""
    vacancy_author = ""
    vacancy_link = ""
    
    def get_vacacy_title(self):
        return self.vacancy_title

    def get_vacancy_salary(self):
        if self.vacancy_salary == "" or self.vacancy_salary == " ":
            return "З/п не задана"
        else:
            return self.vacancy_salary

    # def get_vacancy_tech(self):
    #     return self.vacancy_technology

    def get_vacancy_author(self):
        return self.vacancy_author

    def get_vacancy_link(self):
        return self.vacancy_link


    def show_vacancy(self):
        vacancy_contrainer = f'''Вакансия:{self.get_vacacy_title()}
Зарплата:{self.get_vacancy_salary()}
Разместил(-а): {self.get_vacancy_author()}
Ссылка: {self.get_vacancy_link()}
        '''
        print(vacancy_contrainer)
        return vacancy_contrainer

    def __init__(self, vacancy_title, vacancy_salary, vacancy_author, vacancy_link):
        # self.vacancy_technology = vacancy_technology
        self.vacancy_title = vacancy_title
        self.vacancy_salary = vacancy_salary
        self.vacancy_author = vacancy_author
        self.vacancy_link = vacancy_link
