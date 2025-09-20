import random

def generate_ticket(last_name, destination, departure_time, day):
  ticket_number = random.randint(100000, 999999)
  ticket_price = random.randint(1000, 5000)
  seat = random.randint(1, 200)
  return f"Квиток №{ticket_number}\nПрізвище: {last_name}\nПункт призначення: {destination}\nЧас відправлення: {departure_time}\nДень відправлення: {day}\nЦіна: {ticket_price} гривні\nМісце №{seat}"

last_name = input("Введіть ваше прізвище: ")
destination = input("Введіть пункт призначення: ")
departure_time = input("Введіть час відправлення: ")
day = input("Введіть день відправлення: ")

print(generate_ticket(last_name, destination, departure_time, day))
