import re

def normalize_phone(phone_number):
    like_digitals = re.sub(r'[^\d+]', '', phone_number) # Функція видаляє всі символи, крім цифр та символу '+'.
    # Якщо міжнародний код відсутній, функція додає код '+38'. 
    # Це враховує випадки, коли номер починається з '380' (додається лише '+') 
    # та коли номер починається без коду (додається '+38').
    if like_digitals.startswith('+380'):
        return like_digitals
    elif like_digitals.startswith('380'):
        return '+' + like_digitals
    elif like_digitals.startswith('0'):
        return '+38' + like_digitals
    elif re.fullmatch(r'\d{9}', like_digitals):
        return '+380' + like_digitals
    elif like_digitals.startswith('+'):
        return like_digitals
    else:
        return ''

numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

sanitized_numbers = [normalize_phone(num) for num in numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)