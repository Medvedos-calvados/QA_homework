def is_year_leap(year):

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

user_year = int(input("Введите год: "))
result = is_year_leap(user_year)
print("год", user_year, ":", result)