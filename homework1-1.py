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
    # Підготовка Даних
    birthdays_per_week = defaultdict(list)
    
    # Отримання Поточної Дати
    today = datetime.today().date()
    
    # Перебір Користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        # Оцінка Дати на Цей Рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Порівняння з Поточною Датою
        delta_days = (birthday_this_year - today).days
        
        # Визначення Дня Тижня та коригування для вихідних
        if 0 <= delta_days < 7:
            # Визначення дня тижня дня народження
            birthday_day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
            
            # Перевірка, чи день народження вихідний
            if birthday_day_of_week in ["Saturday", "Sunday"]:
                # Якщо так, зміщуємо на наступний понеділок
                birthday_day_of_week = "Monday"
            
            birthdays_per_week[birthday_day_of_week].append(name)
    
    # Виведення Результату
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")


get_birthdays_per_week(users)