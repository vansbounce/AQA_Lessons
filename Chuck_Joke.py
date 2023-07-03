import requests
url="https://api.chucknorris.io/jokes/categories"
class NewJoke():
    """Создание новой шутки"""
    def __init__(self):
        pass
    def test_your_choice(self):
        """Получение шутки из каждой категории"""
        while True: # Зацикливаем программу
            result = requests.get(url)
            if result.status_code == 200: # Проверяем успешность запроса
                data = result.json()
                category = list(data) #Конвертируем ответ в список
                print("|Шутки про Чака Норриса|")
                print("Доступные категории: " + str(category))
                user_category = input("Введите интересующую вас категорию (или введите 'q' для выхода из программы): ")
                if user_category.lower() == 'q':  #Если пользователь ввел 'q', выходим из цикла
                    break
                if user_category in category: # Проверяем наличие категории в списке
                    joke_url = f"https://api.chucknorris.io/jokes/random?category={user_category}"
                    joke_response = requests.get(joke_url)
                    if joke_response.status_code == 200: # Проверяем успешность запроса
                        joke_data = joke_response.json() # Получаем шутку в формате JSON
                        joke = joke_data["value"] # Извлекаем текст шутки
                        # Выводим шутку на печать
                        print(f"Шутка в категории '{user_category}':")
                        print(joke)
                        print("")
                    else:
                        print("Произошла ошибка при получении шутки.")
                        print(" ")
                else:
                    print("Выбранная категория не найдена.")
                    print(" ")
            else:
                print("Произошла ошибка при выполнении запроса.")
                print(" ")
all_jokes = NewJoke()
all_jokes.test_your_choice()


