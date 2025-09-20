product_name = input("Введіть назву товару: ")
quantity = int(input("Введіть кількість: "))
price = float(input("Введіть ціну за одиницю: "))
quantity_per_day = int(input("Введіть кількість товару проданого за день: "))
quantity_per_week = int(input("Ввдіть кількість товару проданого за тиждень: "))

total_cost = quantity * price
day_cost = quantity_per_day * price
week_cost = quantity_per_week * price

print(f"""
Продукт: {product_name}
Кількість: {quantity}
Вартість: {total_cost}
Сума продажу за день: {day_cost}
Сума продажу за тиждень: {week_cost}
""")
