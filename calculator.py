def calculator():
    while True:
        # Запрашиваем первое число и проверяем ввод на число
        while True:
            try:
                num_1 = float(input("Введите первое число: "))
                break
            except ValueError:
                print("Ошибка! Введите число.")
        # Запрашиваем необходимую операцию
        operator = input("Введите операцию (+, -, *, /): ")
        # Запрашиваем второе число и проверяем ввод на число
        while True:
            try:
                num_2 = float(input("Введите второе число: "))
                break
            except ValueError:
                print("Ошибка! Введите число.")
        # Выполняем операцию и выводим результат
        if operator == "+":
            result = num_1 + num_2
        elif operator == "-":
            result = num_1 - num_2
        elif operator == "*":
            result = num_1 * num_2
        elif operator == "/":
            if num_2 != 0:
                result = num_1 / num_2
            else:
                print("Ошибка! Деление на ноль.")
                continue
        else:
            print("Ошибка! Недопустимая операция.")
            continue
        print("Результат: ", result)
        # Проверяем, хочет ли пользователь продолжить
        choice = input("Хотите продолжить вычисления? (да/нет): ")
        if choice.lower() != "да":
            break
    print("Конец программы.")
calculator()

