from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import importlib_resources



root = Tk()
root.title("Weather App")
root.geometry("1200x600+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)
def getWeather():
    city=textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{location.latitude}{location.longitude}")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    api = "8276ee7c9cbb006971fb86195a55c0d9"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    URL = BASE_URL + "q=" + city + "&appid=" + api

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

        print(f"{city:-^30}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report}")


# icon
image_icon = Image.open("images/logo.png")
photo_icon = ImageTk.PhotoImage(image_icon)
root.iconphoto(False, photo_icon)

#Rounded box image
round_box = Image.open("images/RR1.png")
photo_round_box = ImageTk.PhotoImage(round_box)
Label(root, image=photo_round_box, bg='#57adff').place(x=30, y=110)

# Labels
label1 = Label(root, text="Temperature", font=('Helvetica', 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=('Helvetica', 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=('Helvetica', 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed", font=('Helvetica', 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=('Helvetica', 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

#Search box
#search_image = Image.open("images/SB.png")
#search_photo = ImageTk.PhotoImage(search_image)
#SearchLabel = Label(image=search_photo, bg="#57adff")
#SearchLabel.place(x=270, y=120)

wea_image = Image.open("images/Cloud1.png")
wea_photo = ImageTk.PhotoImage(wea_image)
WeaLabel = Label(image=wea_photo, bg="#57adff")
WeaLabel.place(x=270, y=120)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=340, y=124)
textfield.focus()

search_icon_image = Image.open("images/Layer_6.png")
search_icon_photo = ImageTk.PhotoImage(search_icon_image)
search_icon_button = Button(image=search_icon_photo, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
search_icon_button.place(x=645, y=124)

#Bottom Boc
frame = Frame(root,width=1200,height=160,bg="#212120")
frame.pack(side=BOTTOM)

#Bottom Boxes
firstbox_image = Image.open("images/RR1.png")
firstbox_photo = ImageTk.PhotoImage(firstbox_image)

secondbox_image = Image.open("images/RR2.png")
secondbox_photo = ImageTk.PhotoImage(secondbox_image)

label_firstbox = Label(root, image=firstbox_photo)
label_firstbox.place(x=20, y=330)

label_firstbox2 = Label(root, image=secondbox_photo)
label_firstbox2.place(x=300, y=330)

label_firstbox2 = Label(root, image=secondbox_photo)
label_firstbox2.place(x=400, y=330)

label_firstbox4 = Label(root, image=secondbox_photo)
label_firstbox4.place(x=500, y=330)

label_firstbox5 = Label(root, image=secondbox_photo)
label_firstbox5.place(x=600, y=330)

label_firstbox6 = Label(root, image=secondbox_photo)
label_firstbox6.place(x=700, y=330)

label_firstbox7 = Label(root, image=secondbox_photo)
label_firstbox7.place(x=800, y=330)

#clock
clock=Label(root,font=("Helvetica",30,"bold"),fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",30,"bold"),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat=Label(root,font=("Helvetica",30,"bold"),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)


root.mainloop()
