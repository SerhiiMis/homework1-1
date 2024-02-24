from collections import defaultdict
from datetime import datetime, timedelta


users = [
    {"name": "Ivan Houska", "birthday": datetime(1964, 1, 28)},
    {"name": "Jim Dale", "birthday": datetime(1977, 2, 26)},
    {"name": "Max Kartoon", "birthday": datetime(1974, 2, 14)},
    {"name": "Nicole Best", "birthday": datetime(1980, 2, 25)},
    {"name": "Serhii Soul", "birthday": datetime(1955, 3, 1)},
    {"name": "Bohdan Beniuk", "birthday": datetime(1976, 4, 5)},
    {"name": "Ben Walles", "birthday": datetime(1974, 2, 27)}
]


def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days < 7:
            birthday_day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
            if birthday_day_of_week in ["Saturday", "Sunday"]:
                birthday_day_of_week = "Monday"
            birthdays_per_week[birthday_day_of_week].append(name)
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")


get_birthdays_per_week(users)