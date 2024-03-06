api = "api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

print("For which city?")
CITY = input("City?: ")
URL = BASE_URL + "q=" + CITY + "&appid=" + api

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    # Check if 'main' key exists in the response
    if 'main' in data:
        main = data['main']
        temperature = main.get('temp', 'N/A')
        humidity = main.get('humidity', 'N/A')
        pressure = main.get('pressure', 'N/A')
    else:
        print("Error: 'main' key not found in the response.")
        temperature = humidity = pressure = 'N/A'

    report = data['weather'][0]['description']

    print(f"{CITY:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report}")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")