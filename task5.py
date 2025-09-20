import matplotlib.pyplot as plt

def weather_report(city, temperature, humidity, weather_description):
  return f"Погода в місті {city}:\nТемпература: {temperature}°C\nВологість: {humidity}%\n{weather_description}"

city = input("Введіть назву міста: ")
temperature = float(input("Введіть температуру: "))
humidity = int(input("Введіть вологість: "))
weather_description = input("Введіть опис погоди: ")

print(weather_report(city, temperature, humidity, weather_description))
temp = input("Введіть температуру з понеділка по четверг(через кому): ")
x = ["ПН","ВТ","СР","ЧТ"]
y = [int(t.strip()) for t in temp.split(",")]
plt.plot(x, y, marker = '*')
plt.title(f'Погода міста {city}')
plt.xlabel('Дні тижня')
plt.ylabel('Температура')
plt.show()