import string
def letters_between(user_input):
    all_letters = string.ascii_letters
    start_letter, end_letter = user_input.split('-')
    start_index = all_letters.index(start_letter)
    end_index = all_letters.index(end_letter)
    return all_letters[start_index:end_index + 1]
user_input = input("Введіть дві літери через дефіс (наприклад, a-g): ")
result = letters_between(user_input)
print(f"Символи між введеними літерами: {result}")