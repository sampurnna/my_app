import tkinter as tk
import requests
import time
def getWeather(canvas):
    city = textfield.get()

    api="http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=0d2885ec7aed80ad687e56f6fb3b5768"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']-273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%M", time.gmtime(json_data['sys']['sunrise'] + 19800))
    sunset = time.strftime("%I:%M:%M", time.gmtime(json_data['sys']['sunset'] + 19800))

    final_info= condition + "\n" +str(temp) + "°C"
    final_data="\n" + "Max Temp : " +str(max_temp) + "\n" + "Min Temp : " +str(min_temp) +"\n" +"Pressure : " + str(pressure) +"\n" + "Humidity : " + str(humidity) + "\n" +"Wind Speed : " +str(wind) +"\n" +"Sunrise : " + sunrise+"\n" +"Sunset : " +sunset
    label1.config(text=final_info)
    label2.config(text=final_data)
canvas=tk.Tk()
canvas.geometry("500x500")
canvas.title("Weather app")
f=("arabic",15,"bold")
t=("poppins",35,"bold",)
textfield=tk.Entry(canvas,font =t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1=tk.Label(canvas,font =t)
label1.pack()
label2=tk.Label(canvas,font =f)
label2.pack()
canvas.mainloop()