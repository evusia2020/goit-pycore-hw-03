from datetime import datetime


date = '2020-10-09' 


def get_days_from_today(date):
    try:
        date_in_datetime = datetime.strptime(date, '%Y-%m-%d') 
        current_datetime = datetime.today()
        difference_datetime = current_datetime - date_in_datetime 
        return difference_datetime.days 
    except ValueError:
        return "Помилка: Неправильний формат дати."
print (get_days_from_today(date))