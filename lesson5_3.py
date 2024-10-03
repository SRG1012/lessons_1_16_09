
def calculator():
    while True:
        try:
            func = input("Введіть математичний вираз для обчислення (наприклад, 2+2): ")
            result = eval(func)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Сталася помилка: {e}")
        cont = input("Бажаєте продовжити? (y/yes для продовження, будь-яка інша клавіша для виходу): ").lower()
        if cont not in ["y", "yes"]:
            print("Роботу завершено.")
            break
calculator()


