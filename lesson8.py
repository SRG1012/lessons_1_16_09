
def add_one(digits):
        # Перетворюємо список цифр у ціле число
     number = int(''.join(map(str, digits)))

        # Додаємо 1 до числа
     number += 1

    # Перетворюємо результат назад у список цифр
     return [int(digit) for digit in str(number)]







assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")