import requests
base_url = "https://rahulshettyacademy.com" #базовая урл
key = "?key=qaclick123" #параметр для всех запросов

class TestNewLocation():

    def test_post_new_location(self):
        """Создание новой локации"""
        quantity = int(5) #Цикл на 5 place_id
        for i in range (quantity):
            post_resource = "/maps/api/place/add/json" #Ресурс метода Post
            post_url = base_url + post_resource + key
            print(post_url)
            json_for_create_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }
            result_post = requests.post(post_url, json = json_for_create_new_location)
            print(result_post.text)
            print("Статус код : " + str(result_post.status_code))
            assert 200 == result_post.status_code
            print("Успешно!!! Создана новая локация")
            check_post = result_post.json() #в переменную сохраняем json ответа
            check_info_post = check_post.get("status") #в переменную сохраняем значение поля status
            print("Статус код ответа : " + check_info_post)
            assert check_info_post == "OK"
            print("Статус ответа верен")
            place_id = check_post.get("place_id") #Записываем id локации в переменную
            print("Place_id : " + place_id)
            print("\n")
            f = open("text.txt", "a") #Сохраняем id в файл
            f.write(place_id + "\n")
            f.close()


    # def test_get_new_location(self): # Если вдруг нужно проверить в задании созданные локации
    #     """Проверка создания новой локации"""
    #     get_resource = "/maps/api/place/get/json"
    #     # Открываем файл с построчным списком place_id
    #     with open("text.txt", "r") as file:
    #         place_ids = file.readlines()
    #         # Обрабатываем каждый place_id
    #         for place_id in place_ids:
    #             # Удаляем пробельные символы и символы новой строки
    #             place_id = place_id.strip()
    #             get_url = base_url + get_resource + key + "&place_id=" + place_id
    #             print(get_url)
    #             result_get = requests.get(get_url)
    #             print(result_get.text)
    #             print("Статус код : " + str(result_get.status_code))
    #             assert 200 == result_get.status_code
    #             print("Проверка создания новой локации прошла успешно")
    #             print("\n")

    def test_delete_new_location(self):
        """Удаление новых локаций"""
        delete_resource = "/maps/api/place/delete/json"
        # Открываем файл с построчным списком place_id
        with open("text.txt", "r") as file:
            place_ids = file.readlines()
            # Обрабатываем 2-ю и 4-ю локацию place_id
            for place_id in place_ids[1:5:2]:
                # Удаляем пробельные символы и символы новой строки
                place_id = place_id.strip()
                delete_url = base_url + delete_resource + key
                json_for_delete_new_location = {
                    "place_id": place_id
                }
                print(delete_url)
                print("Place_id" + place_id)
                result_delete = requests.delete(delete_url, json = json_for_delete_new_location)
                print("Статус код : " + str(result_delete.status_code))
                assert 200 == result_delete.status_code
                print("Удаление новой локации прошло успешно")
                print("\n")

    def test_get_delete_location(self):
        """Создание новой локации"""
        get_resource = "/maps/api/place/get/json"
        # Открываем файл с построчным списком place_id
        with open("text.txt", "r") as file:
            place_ids = file.readlines()
            # Обрабатываем каждый place_id
            for place_id in place_ids:
                # Удаляем пробельные символы и символы новой строки
                place_id = place_id.strip()
                get_url = base_url + get_resource + key + "&place_id=" + place_id
                print(get_url)
                result_get = requests.get(get_url)
                print(result_get.text)
                print("Статус код : " + str(result_get.status_code))
                if result_get.status_code == 200:
                    # Записываем place_id в новый файл, если статус код - 200
                    with open("text_2.txt", "a") as f:
                        f.write(place_id + "\n")


new_place = TestNewLocation()
new_place.test_post_new_location()
# new_place.test_get_new_location()
new_place.test_delete_new_location()
new_place.test_get_delete_location()