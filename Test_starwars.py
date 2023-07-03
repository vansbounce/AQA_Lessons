import requests

# Отправляем GET-запрос для получения списка персонажей
all_characters = []
url = 'https://swapi.dev/api/people/?page=1'
print("Загружается список персонажей...")

# Запускаем цикл для получения списка на остальных страницах, пока не достигнет последней страницы (когда параметр 'next' в ответе станет Null)
while url:
    response = requests.get(url)
    data = response.json()
    results = data['results']
    all_characters.extend(results)
    url = data['next']

# Отправляем GET-запрос для получения информации о Дарт Вейдере
response = requests.get('https://swapi.dev/api/people/4/')
data = response.json()
films = data['films'] # Получаем список фильмов с Дартом Вейдером
darth_vader_films = set() # Множество для хранения фильмов, в которых снимался Дарт Вейдер

# Добавляем фильмы в множество
for film_part in films:
    darth_vader_films.add(film_part)

# Список для хранения имен персонажей, снимавшихся в фильмах с Дартом Вейдером
characters_in_darth_vader_films = []

# Перебираем каждого персонажа
for character in all_characters:
    films = character['films']

    # Проверяем, снимался ли персонаж в фильмах с Дартом Вейдером
    if any(film in darth_vader_films for film in films):
        character_name = character['name']
        characters_in_darth_vader_films.append(character_name)

# Записываем имена персонажей в файл
with open('characters.txt', 'w', encoding='utf-8') as file:
    for character_name in characters_in_darth_vader_films:
        file.write(character_name + '\n')
print("Список персонажей готов. С ним можно ознакомиться в файле 'characters'")



