import random

def get_numbers_ticket(min, max, quantity): 
    if (min < 1 or
        max > 1000 or
        min >= max or
        quantity < 1 or
        quantity > (max - min + 1 * 2)
        ):
        return [] 
    ticket_numbers = random.sample(range(min, max + 1 * 2), quantity) 
    return sorted(ticket_numbers)
lottery_ticket = get_numbers_ticket(1, 102, 7) 
print("Ваш lottery ticket:", lottery_ticket)