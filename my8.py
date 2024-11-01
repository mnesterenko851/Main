import requests

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": "metric" 
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        print(f"Температура у {city}: {temp}°C")
        print(f"Опис погоди: {weather_desc.capitalize()}")
    else:
        print("Не вдалося отримати дані про погоду.")
get_weather("Kharkiv")


import pandas as pd
friends_data = {
    "Ім'я": ["Олег", "Олександр", "Іван", "Анна"],
    "Вік": [29, 24, 31, 27],
    "Місто": ["Київ", "Львів", "Одеса", "Харків"]
}
friends_df = pd.DataFrame(friends_data)
print(friends_df)


import mymath
num = 5
print(f"Факторіал числа {num} дорівнює {mymath.factorial(num)}")
fib_num = 7
print(f"{fib_num}-е число Фібоначчі дорівнює {mymath.fibonacci(fib_num)}")


