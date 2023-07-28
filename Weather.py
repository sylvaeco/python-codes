from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root= Tk()
root.title("Weather Software")
root.geometry("480x100")

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=51175B91-BC26-4B8C-B9C8-85161A7CB8B8

def zip_lookup():
 #   zip.get()
 #    zip_label= Label(root,text=zip.get())
 #    zip_label.grid(row = 1, column=0, columnspan=2)

    try:
        api_request= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() +"&distance=5&API_KEY=51175B91-BC26-4B8C-B9C8-85161A7CB8B8")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category= api[0]['Category']['Name']

        if category=="Good":
            weather_color= "#00e400"
        elif category=="Moderate":
            weather_color="#ffff00"
        elif category=="Unhealthy for Sensitive Groups":
            weather_color="#ff7e00"
        elif category=="Unhealthy":
            weather_color="#ff0000"
        elif category=="Very Unhealthy":
            weather_color="#99004c"
        elif category=="Hazardous":
            weather_color="#7e0023"

        root.configure(background=weather_color)
        my_label   = Label(root, text= city + "'s air quaility " + str(quality)+ " " +category, font=('Helvetica, 15'), background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api= "Error...."


myLabel= Label(root, text="The program was built with the Airnow API. Input your zipcode below")
myLabel.grid(row=0, column=0)

zip= Entry(root)
zip.grid(row=1, column=0, sticky=W+E+S+N)

zip_btn=Button(root, text="Lookup Zipcode", command=zip_lookup)
zip_btn.grid(row=1, column=1,  sticky=W+E+S+N)

root.mainloop()
