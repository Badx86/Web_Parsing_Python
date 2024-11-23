from bs4 import BeautifulSoup
import requests

# Получаем содержимое веб-страницы
response = requests.get('https://parsinger.ru/2.1/DOM/example.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Комбинированный поиск: ищем все абзацы с классном "my_class" и атрибутом "data_example"
# paragraphs = soup.select('p.my_class[data-example]')

# Находим все абзацы с атрибутом data-example
# paragraphs = soup.select('p[data-example]')

# Находим все абзацы
paragraphs = soup.find_all('p')

# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')
