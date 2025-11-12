from datetime import datetime, timedelta

def get_upcoming_birthdays(users, fixed_today=None): 
    today = fixed_today or datetime.today().date()
    end_date = today + timedelta(days=7) 
    congratulation_list = [] 

    for user in users: 
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            elif today <= birthday_this_year <= end_date: 
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)
                congratulation_list.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })
            else:
                return []

        except (ValueError, KeyError):
            continue

    return congratulation_list


# Тест з фіксованою датою
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
fixed_today = datetime(2024, 1, 22).date()
upcoming_birthdays = get_upcoming_birthdays(users, fixed_today)
print("Список привітань на цьому тижні:", upcoming_birthdays)