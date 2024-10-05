def format_time(seconds):
    seconds_in_minute = 60
    seconds_in_hour = 60 * 60
    seconds_in_day = 24 * 60 * 60
    days, remainder = divmod(seconds, seconds_in_day)
    hours, remainder = divmod(remainder, seconds_in_hour)
    minutes, seconds = divmod(remainder, seconds_in_minute)
    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"
    formatted_time = (
            f"{days} {day_word}, " +
            f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    return formatted_time
user_input = int(input("Введіть кількість секунд (0 <= секунд < 8640000): "))
result = format_time(user_input)
print(f"Час у форматі: {result}")
