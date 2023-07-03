import requests
url="https://api.chucknorris.io/jokes/categories"
result = requests.get(url)
data = result.json()
category = list(data)#конвертируем ответ в список
print("Список категорий: " + str(category))
print("Запрашиваем по одной шутке из каждой категории:")
class NewJoke():
    """Создание новой шутки"""
    def __init__(self):
        pass
    def test_all_categories_jokes(self):
        """Получение шутки из каждой категории"""
        base_url = 'https://api.chucknorris.io/jokes/random?category='
        for cat in category: #Проходимся циклом по списку, добавляя к базовому урлику каждую категорию
            url = base_url + cat
            response = requests.get(url)
            print("url: " + url)
            joke = response.json()['value']
            print(f"Категория: {cat}")
            print(f"Шутка: {joke}")
            print('===')
            assert 200 == response.status_code #Проверка на статус код
            print("Статус код : " + str(response.status_code))
all_jokes = NewJoke()
all_jokes.test_all_categories_jokes()


