
import requests
from bs4 import BeautifulSoup


def remove_eng(dat):
    eng = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    str = dat.translate({ord(i): None for i in eng})
    return str


def web(page,WebUrl):
    num=1
    dat = ""
    F = open("data.txt", 'a', encoding="utf8")
    while(num<=page):
        url = WebUrl + str(num)

        num+=1
        code = requests.get(url)
        plain = code.text

        s = BeautifulSoup(plain,"lxml")
        for link in s.findAll('a', {'class': 'link_overlay'}):
            tet = "https://www.prothomalo.com"+link.get('href')
            dat+=get_single_item(tet)
            str2 = remove_eng(dat)
            F.write(str2)

def get_single_item(tet):

    txt=""
    url2 = tet
    code2 = requests.get(url2)
    plain2 = code2.text
    s2 = BeautifulSoup(plain2, "lxml")

    for link in s2.findAll('p'):
        txt = txt + str(link.string)

    return txt

web(1,'https://www.prothomalo.com/archive?page=')