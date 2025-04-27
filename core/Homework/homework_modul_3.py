"""Перше завдання
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою."""

from datetime import datetime


def get_days_from_today(date):

    try:
        format_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return ValueError

    date_today = datetime.today().date()
    find_date_days = date_today - format_date
    return find_date_days.days

print(get_days_from_today("2025-4-20"))

"""Друге завдання"""
import random
def get_numbers_ticket(min_num, max_num, quantity):

    if min_num < 1 or max_num > 1000 or quantity > (max_num - min_num + 1):
        return []


    lott_num = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(lott_num)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)



