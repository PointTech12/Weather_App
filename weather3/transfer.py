import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from time import strftime

def get_weather():
    city = city_entry.get()

    # API request
    api_key = "api_key"
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

        # Update time label
        update_time_label()
    else:
        city_label.config(text=f"Error: Unable to fetch data. Status code: {response.status_code}")
        temperature_label.config(text="")
        humidity_label.config(text="")
        pressure_label.config(text="")
        report_label.config(text="")

def update_time_label():
    time_str = strftime("%H:%M %p")
    time_label.config(text=f"Time: {time_str}")
    time_label.after(1000, update_time_label)  # Update time every 1000 milliseconds (1 second)

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("600x300+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

# Style for themed widgets
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))

# Entry for city
city_entry = tk.Entry(root, font=('Helvetica', 12), width=30)
city_entry.place(x=10, y=10)

# Search button
search_button = ttk.Button(root, text="Search", command=get_weather)
search_button.place(x=10, y=50)

# Labels for weather information
city_label = ttk.Label(root, text="", font=('Helvetica', 14))
city_label.place(x=10, y=90)

temperature_label = ttk.Label(root, text="", font=('Helvetica', 12))
temperature_label.place(x=10, y=120)

humidity_label = ttk.Label(root, text="", font=('Helvetica', 12))
humidity_label.place(x=200, y=120)

pressure_label = ttk.Label(root, text="", font=('Helvetica', 12))
pressure_label.place(x=10, y=150)

report_label = ttk.Label(root, text="", font=('Helvetica', 12), wraplength=400)
report_label.place(x=200, y=150)

# Time label
time_label = ttk.Label(root, text="", font=('Helvetica', 12))
time_label.place(x=400, y=10)

# Run the GUI
update_time_label()  # Start updating time label
root.mainloop()
