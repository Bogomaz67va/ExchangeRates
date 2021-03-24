import requests
import xml.etree.ElementTree as ET


class CourseCurrency:
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.get(url)
    tree = ET.fromstring(r.content)

    def __init__(self, number: int, name: str):
        if CourseCurrency.r.status_code == 200:
            self.number = number
            self.name = name
        else:
            print(f"Проверте ссылку {CourseCurrency.url}")
            exit()

    @staticmethod
    def show_course():
        """Выводит курсы валют"""
        for child in CourseCurrency.tree.findall('Valute'):
            print(f"CharCode: {child.find('CharCode').text}, Name: {child.find('Name').text}, "
                  f"Course: {child.find('Value').text}")

    def calculator(self):
        """Отображает валюту в рублях"""
        currency_list = []
        for child in CourseCurrency.tree.findall('Valute'):
            name_currency = child.find('Name').text
            currency = child.find('Value').text
            nominal = child.find('Nominal').text
            char_code = child.find('CharCode').text
            currency_list.append({
                'char_code': char_code,
                'name_currency': name_currency,
                'currency': currency,
                'nominal': nominal
            })

        for item in currency_list:
            if item['char_code'] == self.name:
                currency = item['currency'].replace(',', '.')
                nominal = item['nominal']
                sum_rates = (float(currency) / float(nominal))
                print(f"RUB: {(round(sum_rates, 2) * self.number)} руб.")


CourseCurrency.show_course()
jpy = CourseCurrency(2000, 'JPY')
jpy.calculator()
