#
# from datetime import datetime
#
#
# def string_to_data(data_string):
#     """Перетворює рядок дати у форматі YYYY.MM.DD в об'єкт datetime.date."""
#     try:
#         datetime_object = datetime.strptime(data_string, "%Y.%m.%d")
#         date_object = datetime_object.date()
#         return date_object
#     except ValueError:
#         return "Неправильний формат рядка дати. Очікується YYYY.MM.DD"
#
#
# data_string = "2024.01.01"
# converted_date = string_to_data(data_string)
# print(converted_date)
#
# data_string_wrong_format = "2024-01-01"
# converted_date_wrong = string_to_data(data_string_wrong_format)
# print(converted_date_wrong)

# from datetime import datetime
#
# def string_to_date(date_string):
#     try:
#         datetime_format = datetime.strptime(date_string, "%Y.%m.%d")
#         date_obj = datetime_format.date()
#         return date_obj
#     except ValueError:
#         return "Неправильний формат"
#
# date_string = "2024.01.01"
# converted_date = string_to_date(date_string)
# print(converted_date)


# from datetime import datetime
#
# def string_to_date(date_string):
#     try:
#          datetime_format = datetime.strptime(date_string, "%Y.%m.%d")
#          date_obj = datetime_format.date()
#          return date_obj
#     except ValueError:
#         return "error value"
#
#
#
# def date_to_string(date):
#     date_str = datetime.strftime(date, "%Y.%m.%d")
#     return date_str
#
#
# date_string2 = "2024.01.01"
# converted_date = string_to_date(date_string2)
# print(converted_date)
# date_string2 = date_to_string(converted_date)
# print(date_string2)

# from datetime import datetime
#
#
# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()
#
#
# def prepare_user_list(user_data):
#     users_list = []
#     for u in user_data:
#         name = u["name"]
#         birthday = u["birthday"]
#         date_format = string_to_date(birthday)
#         new_user_in_list = {"name": name, "birthday": date_format}
#         users_list.append(new_user_in_list)
#     return users_list
#
# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]
#
# prepared_users = prepare_user_list(users)
# print(prepared_users)

# from datetime import datetime, timedelta
#
#
# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()
#
#
# def find_next_weekday(start_date, weekday):
#     current_weekday = start_date.weekday()
#     days_ahead = weekday - current_weekday
#     if days_ahead == 0 or days_ahead < 0:
#         days_ahead += 7
#         return start_date + timedelta(days=days_ahead)
#
#
# start_date = string_to_date("2024.03.26")  # Перетворення рядка на дату
# next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
# print(next_monday)
# next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
# print(next_friday)
#
#
#
# start_date = string_to_date("2024.03.26")  # Перетворення рядка на дату
# next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
# print(next_monday)
# next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
# print(next_friday)


"""NEw"""
# from datetime import datetime, date
#
#
# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()
#
#
# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")
#
#
# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list
#
#
# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#
#     return upcoming_birthdays
#
#
# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
# ]
#
# print(get_upcoming_birthdays(prepare_user_list(users, 7)))

# from datetime import datetime, date
#
#
# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()
#
#
# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")
#
#
# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"]).replace})
#     return prepared_list
#
#
# def get_upcoming_birthdays(users, days=7):
#     def get_upcoming_birthdays(users, days=7):
#         upcoming_birthdays = []
#         today = date.today()
#
#         for user in users:
#             # 1. День народження в поточному році
#             birthday_this_year = user["birthday"].replace(year=today.year)
#
#             # 2. Різниця в днях між сьогодні та днем народження
#             days_difference = (birthday_this_year - today).days
#
#             # 3. Перевірка: чи день народження протягом next `days` днів
#             if 0 <= days_difference <= days:
#                 upcoming_birthdays.append({
#                     "name": user["name"],
#                     "congratulation_date": date_to_string(birthday_this_year)
#                 })
#
#         return upcoming_birthdays
#
# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
# ]
#
# prepared = prepare_user_list(users)
# print(get_upcoming_birthdays(prepared, 7))


# from datetime import datetime, date
#
#
# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()
#
#
# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")
#
#
# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list
#
#
# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#
#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)
#         days_difference = (birthday_this_year - today).days
#
#         if 0 <= days_difference <= days:
#             upcoming_birthdays.append({
#                 "name": user["name"],
#                 "congratulation_date": date_to_string(birthday_this_year)
#             })
#
#     return upcoming_birthdays
#
# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
# ]
#
# prepared = prepare_user_list(users)
# print(get_upcoming_birthdays(prepared, 7))


"""5 завдання"""
# from datetime import datetime, timedelta
#
#
# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()
#
#
# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)
#
#
# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5:
#         return find_next_weekday(birthday, 0)
#
#     return birthday

""" 6 завдання """
# from datetime import datetime, date, timedelta
#
#
# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()
#
#
# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")
#
#
# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list
#
#
# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)
#
#
# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5:
#         return find_next_weekday(birthday, 0)
#     return birthday
#
#
# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#
#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)
#         if birthday_this_year < today:
#             birthday_this_year = birthday_this_year.replace(year= today.year + 1)
#
#
#         days_difference = (birthday_this_year - today).days
#         """
#         Додайте на цьому місці перевірку, чи не буде
#         припадати день народження вже наступного року.
#         """
#
#         if 0 <= (birthday_this_year - today).days <= days:
#             congratulation_date = adjust_for_weekend(birthday_this_year)
#             """
#             Додайте перенесення дати привітання на наступний робочий день,
#             якщо день народження припадає на вихідний.
#             """
#
#             congratulation_date_str = date_to_string(congratulation_date)
#             upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
#
#
#     return upcoming_birthdays
#
# users = [
#     {"name": "Bill Gates", "birthday": "1955.5.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.5.22"},
#     {"name": "Sarah Lee", "birthday": "1957.3.23"},
#     {"name": "Jonny Lee", "birthday": "1958.7.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.04.27"}
# ]
#
# prepared_users = prepare_user_list(users)
# print(get_upcoming_birthdays(prepared_users))
#


"""Test"""
# from datetime import datetime
#
# def string_to_date (str_date):
#     return datetime.strptime(str_date, "%Y, %m, %d").date()
#
# def date_to_string (date):
#     return date.strftime("%Y.%m.%d")
#
#
# raw = "1995, 5, 11"
# convert = string_to_date(raw)
# print(f"Це у форматі дата {convert}")
# print("Дата у рядку:", date_to_string(convert))
#
# sentence = "The quick brown fox jumps over the lazy dog"
# length = 0
# for i in sentence:
#     if i !=  " ":
#         length = length + 1
#         print(length)


# sentence = "The quick brown fox jumps over the lazy dog"
# length = len(sentence.replace(" ", ""))
# print(length)

# sentence = "The quick brown fox jumps over the lazy dog"
# length = 0
# for i in sentence:
#     if i != " ":
#         length += 1
#         print(length)


"""робочий код"""
# from datetime import datetime, date, timedelta
#
# #трансформуємо string to data івикористовуємо в другій функції
# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()
#
#
# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")
#
#
# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list
#
#
# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)
#
#
# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5:
#         return find_next_weekday(birthday, 0)
#     return birthday
#
#
# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#
#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)
#         if birthday_this_year < today:
#             birthday_this_year = birthday_this_year.replace(year= today.year + 1)
#
#
#         days_difference = (birthday_this_year - today).days
#         """
#         Додайте на цьому місці перевірку, чи не буде
#         припадати день народження вже наступного року.
#         """
#
#         if 0 <= (birthday_this_year - today).days <= days:
#             congratulation_date = adjust_for_weekend(birthday_this_year)
#             """
#             Додайте перенесення дати привітання на наступний робочий день,
#             якщо день народження припадає на вихідний.
#             """
#
#             congratulation_date_str = date_to_string(congratulation_date)
#             upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
#
#
#     return upcoming_birthdays
#
# users = [
#     {"name": "Bill Gates", "birthday": "1955.5.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.5.22"},
#     {"name": "Sarah Lee", "birthday": "1957.3.23"},
#     {"name": "Jonny Lee", "birthday": "1958.7.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.04.27"}
# ]
#
# prepared_users = prepare_user_list(users)
# print(get_upcoming_birthdays(prepared_users))

