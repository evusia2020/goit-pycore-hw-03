from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядок у дату
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Поточна дата (тільки дата, без часу)
        today = datetime.today().date()
        
        # Різниця між датами
        difference = today - input_date
        
        # Повертаємо кількість днів (може бути від'ємним числом)
        return difference.days
    
    except ValueError:
        return "Невірний формат дати. Використовуйте формат РРРР-ММ-ДД."

import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка валідності параметрів
    if min < 1 or max > 1000 or quantity > (max - min + 1) or quantity <= 0:
        return []
    
    # Генеруємо унікальні числа
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Повертаємо відсортований список
    return sorted(numbers)

random.sample(range(min, max + 1), quantity) #автоматично гарантує унікальність чисел.

#Якщо quantity більша, ніж можливих чисел у діапазоні — повертаємо пустий список.

#Результат завжди буде відсортований.

#Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр і '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number)
    
    # Якщо номер починається з '+380' → залишаємо як є
    if cleaned.startswith("+380"):
        return cleaned
    
    # Якщо номер починається з '380' → додаємо лише '+'
    if cleaned.startswith("380"):
        return "+" + cleaned
    
    # Якщо номер починається з '0' → додаємо '+38'
    if cleaned.startswith("0"):
        return "+38" + cleaned
    
    # Якщо номер не має коду та не починається з нуля → просто додаємо '+38'
    return "+38" + cleaned