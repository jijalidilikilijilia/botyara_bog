from bs4 import BeautifulSoup as bs
import requests as req

def make_url(text):
    #area=1 - Moscow
    #text = Request
    url = 'https://hh.ru/search/vacancy?text='+text+'&area=1'
    return url


def get_hh_title():
    pass

def get_hh_salary():
    pass

def get_hh_author():
    pass

def get_hh_link():
    pass

def get_vacansies_count():
    pass

lang = ["1C", 'C%23', "Kotlin", "Java", "Python"]
# url # = %23

text = lang[1] # C#
url = make_url(text)
print("url: " + url)
request = req.get(url, headers={'User-Agent': 'Custom'})
bsparse = bs(request.text, "lxml")
hh_vacancy_plates = bsparse.find_all('div', 'serp-item')

# f = 1
g = 1
# for i in hh_vacancy_plates:
#     print(str(f) + i.h3.text)
#     f += 1

# print("-------------------------------------")


vacancy_serp_content = bsparse.find('div', id = "a11y-main-content")

