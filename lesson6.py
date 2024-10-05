def multiply_num(n):
    while n > 9:
        result = 1
        for digit in str(n):
            result *= int(digit)
        n = result
    return n
number = int(input("Введіть ціле число: "))
result = multiply_num(number)
print(f"Результат: {result}")