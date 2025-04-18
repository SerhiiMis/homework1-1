from collections import defaultdict
from datetime import datetime, timedelta

def get_birthday_per_week(users):
    """
    Returns a dict mapping weekdays ("Monday", "Tuesday", etc.)
    to lists of users names whose birthday falls within the next 7 days.
    Weekend birthdays (Saturday and Sunday) are grouped into Monday.
    """
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    one_week = today + timedelta(days=7)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        # Move birthday into this calendar year
        birthday_this_year = birthday.replace(year=today.year)

        # If it's already passed, bump to next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Check if it's within the next 7 days
        if today <= birthday_this_year <= one_week:
            weekday = birthday_this_year.strftime("%A")
            # Roll weekends into Monday
            if weekday in ("Saturday", "Sunday"):
                weekday = "Monday"
            birthdays_per_week[weekday].append(name)

    return dict(birthdays_per_week)


if __name__ == "__main__":
    # Example usage
    users = [
        {"name": "Ivan Houska",  "birthday": datetime(1964, 1, 28)},
        {"name": "Jim Dale",     "birthday": datetime(1977, 2, 26)},
        {"name": "Max Kartoon",  "birthday": datetime(1974, 2, 14)},
        {"name": "Nicole Best",  "birthday": datetime(1980, 2, 25)},
        {"name": "Serhii Soul",  "birthday": datetime(1955, 3, 1)},
        {"name": "Bohdan Beniuk","birthday": datetime(1976, 4, 5)},
        {"name": "Ben Walles",   "birthday": datetime(1974, 2, 27)},
        # add a test birthday to see output:
        {"name": "Test User", "birthday": datetime(2004, 4, 24)},
    ]

    print(f"Today is {datetime.today().date()}\n")
    birthdays = get_birthday_per_week(users)

    if not birthdays:
        print("No birthdays this week.")
    else:
        for day, names in birthdays.items():
            print(f"{day}: {', '.join(names)}")