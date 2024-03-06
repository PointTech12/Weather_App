import requests
import tkinter as tk
from PIL import Image, ImageTk

def get_weather():
    city = city_entry.get()

    # API request
    api_key = "8276ee7c9cbb006971fb86195a55c0d9"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    url = f"{base_url}q={city}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extract weather information
        if 'main' in data:
            main = data['main']
            temperature = main.get('temp', 'N/A')
            humidity = main.get('humidity', 'N/A')
            pressure = main.get('pressure', 'N/A')
        else:
            temperature = humidity = pressure = 'N/A'

        report = data['weather'][0]['description']

        # Update labels with weather information
        city_label.config(text=f"City: {city}")
        temperature_label.config(text=f"Temperature: {temperature}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        report_label.config(text=f"Weather Report: {report}")
    else:
        city_label.config(text=f"No city named '{city}' found")
        temperature_label.config(text="")
        humidity_label.config(text="")
        pressure_label.config(text="")
        report_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.title("Weather App")
root.geometry("600x300+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)


# Entry for city
city_entry = tk.Entry(root, font=('Helvetica', 12))
city_entry.pack(pady=10)

# Search button
search_button = tk.Button(root, text="Search", command=get_weather, font=('Helvetica', 12))
search_button.pack(pady=10)

# Labels for weather information
city_label = tk.Label(root, text="", font=('Helvetica', 14))
city_label.pack()

temperature_label = tk.Label(root, text="", font=('Helvetica', 12))
temperature_label.pack()

humidity_label = tk.Label(root, text="", font=('Helvetica', 12))
humidity_label.pack()

pressure_label = tk.Label(root, text="", font=('Helvetica', 12))
pressure_label.pack()

report_label = tk.Label(root, text="", font=('Helvetica', 12))
report_label.pack()

# Run the GUI
root.mainloop()
